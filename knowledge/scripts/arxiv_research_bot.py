# -*- coding: utf-8 -*-
"""
arxiv_research_bot.py

- `knowledge/config/keywords.yaml` のキーワードを読み込み
- Vault 全体 (inbox, archive, research) の Markdown を走査し、既に取得済みの arXiv ID を集合化
- 各キーワードについて arXiv API (Atom フィード) から直近30日以内の論文を取得
- 取得した論文は重複でなければ `knowledge/inbox/academic_papers/` に Markdown で保存
- 保存形式は FrontMatter + 本文 (要旨) を含むシンプルなテンプレート

実行例::
    python arxiv_research_bot.py
"""

import os
import re
import yaml
import feedparser
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# 設定読み込み
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]  # MyBrain ルートディレクトリ
CONFIG_PATH = BASE_DIR / "knowledge" / "config" / "keywords.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

KEYWORDS = cfg.get("keywords", [])
LOOKBACK_DAYS = cfg.get("lookback_days", 30)
OUTPUT_DIR = BASE_DIR / cfg.get("output_dir", "knowledge/inbox/academic_papers")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 既存の arXiv ID を取得 (Vault 全体走査)
# ---------------------------------------------------------------------------
ARXIV_ID_PATTERN = re.compile(r"arxiv\.org/(abs|pdf)/(?P<id>\d{4}\.\d{5}(v\d+)?)", re.IGNORECASE)

def collect_existing_ids_and_names() -> tuple:
    """Vault 配下の markdown から取得済み arXiv ID と、既存のファイル名（拡張子除去、タイムスタンプ除去）を抽出する。
    Returns:
        (set of IDs, set of base filenames)
    """
    ids = set()
    names = set()
    timestamp_pattern = re.compile(r"_(\d{8}_\d{6})(?:_\d+)?$")
    for md_path in BASE_DIR.rglob("*.md"):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        # Extract arXiv IDs
        for match in ARXIV_ID_PATTERN.finditer(text):
            ids.add(match.group("id"))
        # Extract filename stem without timestamp suffix
        stem = md_path.stem
        # Remove trailing timestamp like _20260522_224207 or _20260522_224207_1
        stem = timestamp_pattern.sub('', stem)
        names.add(stem)
    return ids, names

EXISTING_IDS, EXISTING_NAMES = collect_existing_ids_and_names()

# ---------------------------------------------------------------------------
# arXiv から取得
# ---------------------------------------------------------------------------
ARXIV_API_URL = "http://export.arxiv.org/api/query"

def fetch_papers(keyword: str) -> list:
    """キーワードで arXiv API を呼び出し、直近 LOOKBACK_DAYS の論文リストを取得する。"""
    import urllib.parse
    query = f"all:{keyword}"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": 50,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = ARXIV_API_URL + "?" + urllib.parse.urlencode(params)
    feed = feedparser.parse(url)
    papers = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    for entry in feed.entries:
        try:
            published_dt = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if published_dt < cutoff:
            continue
        arxiv_id = entry.id.split('/')[-1]
        if arxiv_id in EXISTING_IDS:
            continue
        papers.append({
            "id": arxiv_id,
            "title": entry.title.strip().replace("\n", " "),
            "authors": [a.name for a in entry.authors] if hasattr(entry, "authors") else [],
            "published": published_dt.strftime("%Y-%m-%d"),
            "summary": entry.summary.strip() if hasattr(entry, "summary") else "",
            "url": entry.link,
        })
    return papers


def is_relevant_paper(paper: dict, cfg: dict) -> bool:
    """判定: Paper がプロジェクトの焦点（Physical-AI, VLA, 自動運転, MLOps, Robotics 等）に合致するか。

    - `focus_terms` が設定にあればそれを優先的に評価。
    - `blocklist_terms` にマッチする語があれば除外（ただし明示的な focus_terms が含まれる場合は許可）。
    - 物理的/エンボディメント語と AI/ロボティクス語の共起があれば許可。
    """
    title = (paper.get('title') or '').lower()
    summary = (paper.get('summary') or '').lower()
    text = title + '\n' + summary

    focus = [t.lower() for t in cfg.get('focus_terms', [])]
    block = [t.lower() for t in cfg.get('blocklist_terms', [])]
    ai_terms = [t.lower() for t in cfg.get('ai_terms', ['ai', 'llm', 'machine learning', 'deep learning', 'neural', 'agent', 'agentic'])]

    # ブロック語があれば、焦点語が含まれない限り除外
    if any(b in text for b in block):
        if any(f in text for f in focus):
            return True
        return False

    # 明示的な focus_terms があれば許可
    if any(f in text for f in focus):
        return True

    # 物理/エンボディメント語と AI/ロボ語の共起を確認
    phys_terms = ['physical', 'physical-ai', 'physical_ai', 'embodiment', 'manipulation', 'manipulator', 'end-effector', 'end effector', 'robot', 'robotic']
    if any(p in text for p in phys_terms) and any(a in text for a in ai_terms):
        return True

    # 最後に、タイトルや要旨に 'robot' など明確なロボティクス語があれば許可
    if any(k in text for k in ['robot', 'robotics', 'autonomous', 'vla', 'vision-language', 'vision language', 'adas', 'autonomous driving']):
        return True

    return False

# ---------------------------------------------------------------------------
# Markdown 保存ユーティリティ
# ---------------------------------------------------------------------------
def sanitize_filename(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", "_", name)
    return name[:200]

def save_paper(paper: dict):
    # Determine base filename without timestamp suffix
    base_name = sanitize_filename(paper['title'])
    # Skip if a file with this base name already exists (ignoring timestamps)
    if base_name in EXISTING_NAMES:
        print(f"Skipping duplicate file name: {base_name}")
        return
    path = OUTPUT_DIR / f"{base_name}.md"
    # If a file with exact name already exists, add timestamp to avoid clash
    if path.exists():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = OUTPUT_DIR / f"{base_name}_{ts}.md"
    front = "---\n"
    front += f"title: \"{paper['title']}\"\n"
    front += f"authors: {paper['authors']}\n"
    front += f"published: {paper['published']}\n"
    front += f"arxiv_id: {paper['id']}\n"
    front += f"url: {paper['url']}\n"
    front += "---\n\n"
    content = front + paper["summary"] + "\n"
    path.write_text(content, encoding="utf-8")
    print(f"Saved: {path}")

# ---------------------------------------------------------------------------
# メインロジック
# ---------------------------------------------------------------------------
def main():
    total = 0
    for kw in KEYWORDS:
        print(f"Fetching papers for keyword: {kw}")
        new_papers = fetch_papers(kw)
        for p in new_papers:
            save_paper(p)
            total += 1
    print(f"\n完了: 新規論文 {total} 件を保存しました。")

if __name__ == "__main__":
    main()
