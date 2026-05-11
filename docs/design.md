# 設計書 - 知識管理・調査自動化システム

## システム構成
1. **Paper Collector (Automated)**: PythonスクリプトによるSemantic Scholar API連携。GitHub Actionsで定期実行。
2. **Trend Integrator (Manual/Semi-Auto)**: ChatGPT, Gemini等の調査結果を `knowledge/inbox/` に手動またはプロンプト経由で統合。
3. **Agent Deep-Dive (Interactive)**: Antigravity Agentを使い、特定の情報をブラウザで深掘り調査。

## 技術スタック
- **言語**: Python 3.10+
- **API**: Semantic Scholar API
- **ライブラリ**: `requests`, `python-frontmatter` (Markdown操作), `PyYAML`
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

## パス構成
- スクリプト: `knowledge/scripts/research_bot.py`
- 設定ファイル: `knowledge/config/keywords.yaml`
- 出力先 (論文): `knowledge/inbox/academic_papers/`
