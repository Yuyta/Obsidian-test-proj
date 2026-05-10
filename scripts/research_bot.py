import os
import requests
import yaml
import frontmatter
from datetime import datetime
import re

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
        response = requests.get(url, params=params)
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
    
    filename = sanitize_filename(f"{year if year else 'Unknown'}_{title[:50]}.md")
    filepath = os.path.join(output_dir, filename)
    
    # Duplicate check
    if os.path.exists(filepath):
        print(f"Skipping (already exists): {filename}")
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

def main():
    config = load_config("config/keywords.yaml")
    keywords = config.get("keywords", [])
    limit = config.get("search_limit_per_keyword", 3)
    lookback_days = config.get("lookback_days", 7)
    output_dir = config.get("output_dir", "Research/Inbox")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for kw in keywords:
        print(f"Searching for: {kw} (past {lookback_days} days)")
        papers = search_papers(kw, limit=limit, lookback_days=lookback_days)
        for paper in papers:
            save_paper_as_md(paper, output_dir, kw)
        time.sleep(2) # Delay between keywords

if __name__ == "__main__":
    main()
