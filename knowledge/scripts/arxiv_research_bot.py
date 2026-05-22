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
from datetime import datetime, timedelta
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
ARXIV_ID_PATTERN = re.compile(r"arxiv\.org/(abs|pdf)/(?P<id>\d{4}\.\d{5}(v\d+)? )", re.IGNORECASE)

def collect_existing_ids() -> set:
    """Vault 配下の markdown から取得済み arXiv ID を抽出する。"""
    ids = set()
    for md_path in BASE_DIR.rglob("*.md"):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        for match in ARXIV_ID_PATTERN.finditer(text):
            ids.add(match.group("id"))
    return ids

EXISTING_IDS = collect_existing_ids()

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
    cutoff = datetime.utcnow() - timedelta(days=LOOKBACK_DAYS)
    for entry in feed.entries:
        try:
            published_dt = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
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

# ---------------------------------------------------------------------------
# Markdown 保存ユーティリティ
# ---------------------------------------------------------------------------
def sanitize_filename(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", "_", name)
    return name[:200]

def save_paper(paper: dict):
    filename = sanitize_filename(paper["title"]) + ".md"
    path = OUTPUT_DIR / filename
    # 重複防止: 同名があればタイムスタンプ付与
    if path.exists():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = OUTPUT_DIR / f"{sanitize_filename(paper['title'])}_{ts}.md"
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
