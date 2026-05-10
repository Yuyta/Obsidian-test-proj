# 設計書 - 論文調査自動化

## システム構成
1. **Agent Deep-Dive (Interactive)**: Antigravityのブラウザ操作機能を使い、手動で指示を出して深掘りする。
2. **Scheduled Collector (Automated)**: PythonスクリプトによるAPI連携。GitHub Actionsで定期実行し、結果をGit経由または直接Vaultに書き込む。

## 技術スタック
- **言語**: Python 3.10+
- **API**: Semantic Scholar API, Arxiv API
- **ライブラリ**: `requests`, `pydantic` (データ構造), `python-frontmatter` (Markdown操作)
- **自動化**: GitHub Actions

## アーキテクチャ
- **Collector**: 検索キーワードを基に論文一覧を取得。
- **Parser**: 取得したデータをObsidian向けのMarkdownに変換。
- **Store**: 重複チェックを行い、ファイルを書き出し。

## データ設計 (Obsidian Frontmatter)
```yaml
---
title: "論文タイトル"
authors: ["著者1", "著者2"]
year: 2026
doi: "10.xxx/xxx"
url: "https://..."
status: "Inbox"
tags: ["paper", "mlops"]
---
# Summary
...
```

## 処理フロー
1. `config.yaml`から検索キーワードを取得。
2. APIを叩いて最新N件の情報を取得。
3. Vault内の既存ファイルの`doi`または`url`をチェックして重複排除。
4. Markdownファイルを生成し、`Research/Inbox/`に保存。

## エラーハンドリング
- APIのレートリミット到達時はリトライまたは待機。
- ネットワークエラー時はログを出力して終了。
