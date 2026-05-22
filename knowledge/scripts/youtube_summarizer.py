import os
import yaml
import feedparser
import yt_dlp
import google.generativeai as genai
from datetime import datetime
import re
import time
import json

from pathlib import Path

# 設定
BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_PATH = BASE_DIR / "knowledge" / "config" / "youtube_channels.yaml"
OUTPUT_DIR = BASE_DIR / "knowledge" / "inbox" / "youtube"
GEMINI_MODEL = "gemini-1.5-flash"

EXISTING_VIDEO_IDS = set()

def collect_existing_video_ids(vault_root):
    """Vault配下のmarkdownファイルを走査し、既存のYouTubeビデオID（frontmatterのid値またはファイル名から）を収集する。"""
    id_pattern = re.compile(r'id:\s*"(?P<id>[a-zA-Z0-9_-]{11})"')
    timestamp_pattern = re.compile(r"_(\d{8}_\d{6})(?:_\d+)?$")
    
    for md_path in Path(vault_root).rglob("*.md"):
        # ファイルの中身の `id: "xxx"` をチェック
        try:
            text = md_path.read_text(encoding="utf-8")
            found = False
            for match in id_pattern.finditer(text):
                EXISTING_VIDEO_IDS.add(match.group("id"))
                found = True
            if found:
                continue
        except Exception:
            pass
        
        # 中身が読めない、またはidが見つからない場合はファイル名から推測
        stem = md_path.stem
        # タイムスタンプサフィックスを除去
        stem = timestamp_pattern.sub('', stem)
        # YouTubeのIDは通常11文字
        if len(stem) == 11:
            EXISTING_VIDEO_IDS.add(stem)

def setup_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(GEMINI_MODEL)

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_video_subtitles(video_url):
    ydl_opts = {
        'skip_download': True,
        'writeautomaticsub': True,
        'writesubtitles': True,  # 手動アップロードされた日本語字幕も対象にする
        'subtitleslangs': ['ja'],
        'quiet': True,
        'no_warnings': True,
    }
    
    # 一時ファイル名のプレフィックスを絶対パスで設定
    temp_sub_file = str(BASE_DIR / f"temp_sub_{int(time.time())}")
    vtt_file = f"{temp_sub_file}.ja.vtt"
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            title = info.get('title', 'Unknown Title')
            upload_date = info.get('upload_date', 'Unknown Date')
            
            # 字幕の取得（日本語を優先）
            subtitles = ""
            if 'requested_subtitles' in info and 'ja' in info['requested_subtitles']:
                sub_path = info['requested_subtitles']['ja']['url']
                pass

            # 実際にはyt-dlpで字幕ファイルを一度ダウンロードして読み込むのが確実
            # GitHub Actions上では一時ファイルとして扱う
            ydl_opts['outtmpl'] = temp_sub_file
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl_down:
            ydl_down.download([video_url])
        
        # vttファイルを読み込む
        if os.path.exists(vtt_file):
            with open(vtt_file, "r", encoding="utf-8") as f:
                content = f.read()
            # VTTのタグを除去してテキストのみ抽出
            text = re.sub(r'<[^>]+>', '', content)
            text = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*\n', '', text)
            text = "\n".join(list(dict.fromkeys([line.strip() for line in text.split('\n') if line.strip()])))
            return title, upload_date, text
        
        return title, upload_date, None
    except Exception as e:
        print(f"Error getting subtitles for {video_url}: {e}")
        return None, None, None
    finally:
        # 一時ファイルを確実に削除する
        if os.path.exists(vtt_file):
            try:
                os.remove(vtt_file)
            except Exception as e:
                print(f"Warning: Could not remove temp file {vtt_file}: {e}")

def summarize_video(model, title, transcript):
    prompt = f"""
以下のYouTube動画の文字起こしを元に、要約を作成してください。

タイトル: {title}

# 要約ガイドライン:
- 日本語で出力してください。
- 読者が内容を短時間で理解できるように構造化してください。
- 重要なポイントを箇条書きで抽出してください。
- 専門用語があれば必要に応じて解説を含めてください。

# 出力形式:
## 概要
（ここには動画全体の概要を2-3文で記述）

## 主要なポイント
- （ポイント1）
- （ポイント2）
...

## 詳細・学び
（より深い内容や、実務に役立つ知識など）

## 関連キーワード
- （キーワード1）
- （キーワード2）

---
文字起こしデータ:
{transcript}
"""
    response = model.generate_content(prompt)
    return response.text

def main():
    # 出力先ディレクトリが存在しない場合は作成
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 既存のYouTube動画IDをVault全体から収集
    collect_existing_video_ids(BASE_DIR)

    config = load_config()
    model = setup_gemini()

    for channel in config['channels']:
        print(f"Checking channel: {channel['name']}")
        rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}"
        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            video_id = entry.yt_videoid
            video_url = entry.link
            filename = OUTPUT_DIR / f"{video_id}.md"

            # 重複チェック（Vault全体にすでに存在するIDか、またはinboxに同じファイル名が存在する場合）
            if video_id in EXISTING_VIDEO_IDS or filename.exists():
                continue

            print(f"New video found: {entry.title}")
            title, upload_date, transcript = get_video_subtitles(video_url)

            if not transcript:
                print(f"Could not get transcript for {video_id}. Skipping.")
                continue

            summary = summarize_video(model, title, transcript)

            # Markdownファイル作成
            md_content = f"""---
title: "{title}"
url: "{video_url}"
channel: "{channel['name']}"
upload_date: "{upload_date}"
id: "{video_id}"
tags: ["youtube", "summary", "{channel['handle'].replace('@', '')}"]
---

# {title}

URL: {video_url}
投稿日: {upload_date}

{summary}

## 元の文字起こし（一部抜粋）
{transcript[:1000]}...
"""
            with open(filename, "w", encoding="utf-8") as f:
                f.write(md_content)
            print(f"Saved summary to {filename}")
            
            # APIレートリミットを考慮して少し待機
            time.sleep(5)

if __name__ == "__main__":
    main()
