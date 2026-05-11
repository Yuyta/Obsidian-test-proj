# 要件定義書 - 知識管理システム（Knowledge Management System）

## 概要
最新の論文および市場動向（ChatGPT, Gemini等）を自動・手動で集約し、ObsidianのVault（ナレッジベース）に構造化された形式で保存・整理するシステム。

## 背景
- 手動での論文調査や市場動向の追跡は時間がかかる。
- ChatGPTやGeminiからの調査結果を効率的にナレッジベースに統合したい。
- 調査した内容をObsidianにまとめ、横断的に整理・考察（Synthesis）したい。

## スコープ
- **論文調査**: Semantic Scholar APIを利用した自動収集。
- **市場動向調査**: ChatGPT, Gemini, NotebookLMからのインプット統合。
- **YouTube調査**: 特定チャンネルの新着動画の自動要約と保存。
- **知識整理**: InboxからResearch、さらにSynthesis（考察）への昇華プロセス。
- **自動化**: GitHub Actionsによる定期実行。

## 機能要件
- **検索機能**: 指定したキーワードに基づき最新の論文を検索する（Semantic Scholar API）。
- **外部インプット統合**: ChatGPTやGeminiからの出力を `knowledge/inbox/` 配下の適切なフォルダに格納する。
- **YouTube連携**:
    - RSSフィードによる新着動画検知。
    - `yt-dlp` による字幕取得。
    - Gemini APIによる自動要約。
- **Obsidian連携**:
    - 論文: `knowledge/inbox/academic_papers/`
    - YouTube要約: `knowledge/inbox/youtube/`
    - 市場動向: `knowledge/inbox/chatgpt/`, `knowledge/inbox/gemini/` 等
- **重複排除**: 既にVault内に存在する論文はスキップする。
- **定期実行**: 論文調査を週次で自動実行する。

## 非機能要件
- **ディレクトリ構造の保守**: 定義された `knowledge/` 階層を維持する。
- **安定性**: APIを利用し、レートリミットを考慮した実装。
- **拡張性**: 新しいインプットソース（例: WebClips）を容易に追加可能にする。

## ディレクトリ構造（標準）
```
knowledge/
├── inbox/                 # 生データ投入
├── research/              # 整理済み調査
├── synthesis/             # 横断整理・考察
├── skills/                # Antigravity Skills
├── templates/             # Obsidian テンプレート
├── scripts/               # 運用スクリプト
├── daily/                 # デイリーノート
└── config/                # 設定ファイル
```
