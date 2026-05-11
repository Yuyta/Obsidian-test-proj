import os
import yaml
import feedparser
import yt_dlp
import google.generativeai as genai
from datetime import datetime
import re
import time
import json

# 設定
CONFIG_PATH = "knowledge/config/youtube_channels.yaml"
OUTPUT_DIR = "knowledge/inbox/youtube"
GEMINI_MODEL = "gemini-1.5-flash"

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
        'subtitleslangs': ['ja'],
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            title = info.get('title', 'Unknown Title')
            upload_date = info.get('upload_date', 'Unknown Date')
            
            # 字幕の取得（日本語を優先）
            subtitles = ""
            if 'requested_subtitles' in info and 'ja' in info['requested_subtitles']:
                sub_path = info['requested_subtitles']['ja']['url']
                # yt-dlpで直接テキスト化するのは難しいため、別の方法や簡易的なパースが必要になる場合がある
                # ここでは簡易的にinfoから取得できる範囲か、あるいは事後処理を検討
                # 実際には --get-subs 的な動作が必要
                pass

            # 実際にはyt-dlpで字幕ファイルを一度ダウンロードして読み込むのが確実
            # GitHub Actions上では一時ファイルとして扱う
            temp_sub_file = f"temp_sub_{int(time.time())}"
            ydl_opts['outtmpl'] = temp_sub_file
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_down:
                ydl_down.download([video_url])
            
            # vttファイルを読み込む
            vtt_file = f"{temp_sub_file}.ja.vtt"
            if os.path.exists(vtt_file):
                with open(vtt_file, "r", encoding="utf-8") as f:
                    content = f.read()
                # VTTのタグを除去してテキストのみ抽出
                text = re.sub(r'<[^>]+>', '', content)
                text = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*\n', '', text)
                text = "\n".join(list(dict.fromkeys([line.strip() for line in text.split('\n') if line.strip()])))
                os.remove(vtt_file)
                return title, upload_date, text
            
            return title, upload_date, None
    except Exception as e:
        print(f"Error getting subtitles for {video_url}: {e}")
        return None, None, None

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
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    config = load_config()
    model = setup_gemini()

    for channel in config['channels']:
        print(f"Checking channel: {channel['name']}")
        rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}"
        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            video_id = entry.yt_videoid
            video_url = entry.link
            filename = f"{OUTPUT_DIR}/{video_id}.md"

            if os.path.exists(filename):
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
