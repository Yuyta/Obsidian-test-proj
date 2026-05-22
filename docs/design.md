# 設計書 - 知識管理・調査自動化システム

## システム構成
1. **Paper Collector (Automated)**: PythonスクリプトによるSemantic Scholar API連携。GitHub Actionsで定期実行。
2. **Trend Integrator (Manual/Semi-Auto)**: ChatGPT, Gemini等の調査結果を `knowledge/inbox/` に手動またはプロンプト経由で統合。
3. **YouTube Summarizer (Automated)**: YouTube RSSフィードを監視し、字幕をAI要約。
4. **Agent Deep-Dive (Interactive)**: Antigravity Agentを使い、特定の情報をブラウザで深掘り調査。

## 技術スタック
- **言語**: Python 3.10+
- **API**: Semantic Scholar API, Gemini API
- **ライブラリ**: `requests`, `python-frontmatter`, `PyYAML`, `feedparser`, `yt-dlp`, `google-generativeai`
- **自動化**: GitHub Actions

## アーキテクチャ
- **Collector**: `knowledge/config/keywords.yaml` からキーワードを取得し、論文を検索。
- **Integrator**: 市場動向等の外部知見を構造化Markdownとして整理。
- **Refinement Process**: 
    - `inbox/` (未整理) 
    - → `research/` (カテゴリ分類・要約)
    - → `synthesis/` (横断考察・戦略策定)

## データ設計 (Obsidian Frontmatter)
### 論文データ
```yaml
---
title: "論文タイトル"
authors: ["著者1", "著者2"]
year: 2026
doi: "10.xxx/xxx"
url: "https://..."
status: "Inbox"
tags: ["paper", "automated-research"]
---
```

## 処理フロー
1. **論文収集**:
    - `knowledge/scripts/research_bot.py` を実行。
    - APIから最新論文を取得し、重複チェック。
    - `knowledge/inbox/academic_papers/` に保存。
2. **市場動向統合**:
    - ChatGPT等の出力をコピー、またはAgentに依頼して `knowledge/inbox/chatgpt/` 等に保存。
3. **知識の昇華**:
    - 定期的に `inbox/` を確認し、有用な情報を `research/` の各分野（mlops, robotics等）へ移動・整理。
    - 複数の情報を元に `synthesis/` でトレンド分析や戦略を執筆。
4. **inbox整理・アーカイブ処理（仕様変更）**:
    - `knowledge/scripts/inbox_organizer.py` を実行。
    - `knowledge/inbox/` の各サブフォルダ（`academic_papers`, `chatgpt`, `gemini`, `youtube` 等）に残った（または処理済みの）ファイルを、情報源がわかるように `knowledge/archive/<情報源>/` 配下に移動する。
    - 移動先のフォルダが存在しない場合は自動で作成する。
5. **エージェント自律循環フロー**:
    - エージェント（Antigravity）は、`Collector` や `Summarizer` で `inbox/` に集めた生データを自律的に読み込む。
    - 読み込んだ生データを要約・統合した上で、`research/` 配下のカテゴリ別フォルダ（例: `mlops`, `robotics` 等）に成果物（Markdownノート）を作成・更新する。
    - 成果物作成が完了したら、`inbox_organizer.py` をトリガーしてインボックスをクリアし、一連のサイクルを完結させる。


## パス構成
- スクリプト (YouTube): `knowledge/scripts/youtube_summarizer.py`
- スクリプト (整理・アーカイブ): `knowledge/scripts/inbox_organizer.py`
- 設定ファイル (キーワード): `knowledge/config/keywords.yaml`
- 設定ファイル (YouTube): `knowledge/config/youtube_channels.yaml`
- 出力先 (論文): `knowledge/inbox/academic_papers/`
- 出力先 (YouTube): `knowledge/inbox/youtube/`
- 出力先 (アーカイブ): `knowledge/archive/<情報源>/`
