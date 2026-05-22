import os
import requests
import yaml
import frontmatter
from datetime import datetime
import re
from pathlib import Path

EXISTING_TITLES = set()
EXISTING_DOIS = set()

def collect_existing_papers(vault_root):
    """Vault配下のmarkdownファイルから、既存の論文タイトル（小文字化）とDOIを収集する。"""
    timestamp_pattern = re.compile(r"_(\d{8}_\d{6})(?:_\d+)?$")
    doi_pattern = re.compile(r"doi:\s*\"?(?P<doi>10\.\d{4,9}/[-._;()/:A-Z0-9]+)\"?", re.IGNORECASE)
    
    for md_path in Path(vault_root).rglob("*.md"):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
            
        # DOIの抽出
        for match in doi_pattern.finditer(text):
            EXISTING_DOIS.add(match.group("doi").lower())
            
        # ファイル名からベース名を取得
        stem = md_path.stem
        # タイムスタンプサフィックスの除去 (_20260522_224207 等)
        stem = timestamp_pattern.sub('', stem)
        EXISTING_TITLES.add(stem.lower())

def sanitize_filename(filename):
    # Remove characters that are not allowed in filenames
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

import time
from datetime import datetime, timedelta

def search_papers(query, limit=5, lookback_days=7, retry_count=3):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=lookback_days)
    date_range = f"{start_date.strftime('%Y-%m-%d')}:{end_date.strftime('%Y-%m-%d')}"
    
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,url,abstract,externalIds,publicationDate",
        "publicationDateOrYear": date_range
    }
    
    for i in range(retry_count):
        try:
            response = requests.get(url, params=params, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return []
        if response.status_code == 200:
            return response.json().get("data", [])
        elif response.status_code == 429:
            wait_time = (i + 1) * 5
            print(f"Rate limited (429). Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Error searching for {query}: {response.status_code}")
            return []
    return []

def save_paper_as_md(paper, output_dir, keyword):
    title = paper.get("title", "Untitled")
    authors = [a.get("name") for a in paper.get("authors", [])]
    year = paper.get("year")
    url = paper.get("url")
    abstract = paper.get("abstract", "No abstract available.")
    doi = paper.get("externalIds", {}).get("DOI")
    
    filename_base = sanitize_filename(f"{year if year else 'Unknown'}_{title[:50]}")
    if filename_base.lower() in EXISTING_TITLES:
        print(f"Skipping (already exists by title): {filename_base}")
        return
        
    if doi and doi.lower() in EXISTING_DOIS:
        print(f"Skipping (already exists by DOI): {doi}")
        return

    filename = f"{filename_base}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Duplicate check
    if os.path.exists(filepath):
        print(f"Skipping (already exists by path): {filename}")
        return

    # Create frontmatter
    post = frontmatter.Post(abstract)
    post['title'] = title
    post['authors'] = authors
    post['year'] = year
    post['doi'] = doi
    post['url'] = url
    post['status'] = "Inbox"
    post['tags'] = ["paper", "automated-research", keyword.replace(" ", "-")]
    post['fetched_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add Internal Links for Obsidian Graph
    # This ensures the paper is connected to the keyword's note
    content = f"\n\n## Connections\n- Topic: [[{keyword}]]\n- Type: [[Research Paper]]\n\n## Abstract\n{abstract}\n"
    post.content = content

    with open(filepath, 'wb') as f:
        frontmatter.dump(post, f)
    print(f"Saved: {filename}")

def is_relevant_paper(paper, config):
    """Determine if a paper is relevant to the project's focus (Physical-AI, VLA, autonomous driving, MLOps, robotics).

    Uses a combination of allow-terms and co-occurrence rules and a blocklist to avoid medical/clinical/non-embodiment hits.
    """
    title = (paper.get('title') or '').lower()
    abstract = (paper.get('abstract') or '').lower()
    text = title + '\n' + abstract

    # Load filters from config or set sensible defaults
    cfg_focus = [t.lower() for t in config.get('focus_terms', [
        'physical ai', 'physical-ai', 'vla', 'vision-language', 'vision language', 'vision-language-action',
        'vision language action', 'autonomous driving', 'autonomous vehicle', 'adas', 'mlops', 'mlo ps', 'robot', 'robotics',
        'manipulation', 'manipulator', 'end-effector', 'kinematics'
    ])]
    cfg_ai = [t.lower() for t in config.get('ai_terms', [
        'ai', 'llm', 'machine learning', 'deep learning', 'neural', 'agent', 'agentic', 'vln'
    ])]
    cfg_block = [t.lower() for t in config.get('blocklist_terms', [
        'asthma', 'biopsy', 'clinic', 'clinical', 'patient', 'disease', 'epidemic', 'infection', 'hospital', 'covid', 'cancer', 'influenza'
    ])]

    # If blocklist present in text, consider not relevant unless explicit focus term present
    if any(b in text for b in cfg_block):
        if any(f in text for f in cfg_focus):
            return True
        return False

    # If an explicit focus term appears, keep
    if any(f in text for f in cfg_focus):
        return True

    # If physical/embodiment terms co-occur with AI/robotics terms, keep
    phys_terms = ['physical', 'embodiment', 'manipulation', 'manipulator', 'end-effector', 'end effector', 'robot', 'robotic']
    if any(p in text for p in phys_terms) and any(a in text for a in cfg_ai):
        return True

    # Otherwise consider it irrelevant
    return False

def main():
    # スクリプトの場所を基準に設定ファイルのパスを特定
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vault_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    config_path = os.path.join(script_dir, "..", "config", "keywords.yaml")
    
    # 既存の論文情報をVault全体から収集
    collect_existing_papers(vault_root)
    
    config = load_config(config_path)
    keywords = config.get("keywords", [])
    limit = config.get("search_limit_per_keyword", 3)
    lookback_days = config.get("lookback_days", 7)
    
    # 出力先ディレクトリをVaultルートからの相対パスとして設定
    rel_output_dir = config.get("output_dir", "knowledge/inbox/academic_papers")
    output_dir = os.path.join(vault_root, rel_output_dir)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    for kw in keywords:
        print(f"Searching for: {kw} (past {lookback_days} days)")
        papers = search_papers(kw, limit=limit, lookback_days=lookback_days)
        for paper in papers:
            try:
                if not is_relevant_paper(paper, config):
                    print(f"Skipping (not relevant to Physical-AI/etc): {paper.get('title')}")
                    continue
            except Exception as e:
                print(f"Relevance check failed, saving by default: {e}")
            save_paper_as_md(paper, output_dir, kw)
        time.sleep(2) # Delay between keywords

if __name__ == "__main__":
    main()
