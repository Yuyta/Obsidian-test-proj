# 要件定義書 - 論文調査自動化（Paper Research Automator）

## 概要
最新の論文を自動的に調査し、ObsidianのVault（ナレッジベース）に構造化されたMarkdown形式で保存するシステム。

## 背景
- 手動での論文調査は時間がかかる。
- 調査した内容をObsidianにまとめる作業を効率化したい。
- 定期的に最新の技術トレンドをキャッチアップしたい。

## スコープ
- 論文検索（Google Scholar, Semantic Scholar, Arxiv等）
- 情報抽出・要約（タイトル、著者、DOI、Abstract、貢献、課題）
- ObsidianへのMarkdown出力
- 定期実行（GitHub Actions等）

## 機能要件
- **検索機能**: 指定したキーワードに基づき最新の論文を検索する。
- **抽出・要約機能**: 論文のメタデータと内容を抽出し、要約する。
- **Obsidian連携**: Obsidianの特定のフォルダ（`/Research/Inbox/`）にMarkdownファイルを生成する。
- **重複排除**: 既にVault内に存在する論文はスキップする。
- **定期実行**: 週次または日次で自動実行する。

## 非機能要件
- **安定性**: スクレイピングによるブロックを回避するため、可能な限りAPI（Semantic Scholar等）を利用する。
- **カスタマイズ性**: Markdownテンプレートをユーザーが変更可能にする。

## 制約条件
- Google Scholarを直接スクレイピングする場合、IP制限やCAPTCHAの可能性がある。
- 定期実行にはGitHub Actionsなどの外部実行環境が必要。

## 未確定事項
- 論文の全文（PDF）を読み取るか、Abstractのみにするか（API制限やコストの観点）。
- Obsidianの既存メモとの重複検知ロジック（DOIでの一致確認など）。
