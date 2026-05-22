**収集・昇華・整理ワークフロー（inbox→research）**

以下は `SKILL.md` を基にまとめた運用ガイドライン（実践向け）です。目的は `knowledge/inbox/` に集められた情報を自律的かつ再現可能に `knowledge/research/` に構造化・統合することです。

- **目的:** `inbox` の新着を定期的に取り込み、重要な知見を階層化されたリサーチノートへ昇華し、アーカイブを整理する。

**1. 集める（Collection）**
- **実行頻度:** 毎日または起動時に自動化スクリプトを実行。
- **主要スクリプト:** `arxiv_research_bot.py`, `research_bot.py`, `youtube_summarizer.py`。
- **入力先:** `knowledge/inbox/` 以下のフォルダ（`academic_papers/`, `chatgpt/`, `webclips/` など）。
- **メタデータ:** 取り込み時に `title`,`authors`,`url`,`fetched_at`,`tags` を付与する（既に存在するテンプレートに合わせる）。

**2. 昇華する（Synthesis & Refinement）**
- **分類ルール:** トピック（例: `mlops`, `robotics`, `ai-agent`, `Physical-AI`）ごとに `knowledge/research/<topic>/YYYYMMDD_<short-title>.md` を作成。
- **フォーマット（最低限）:** 概要（要点3-5行）、主要貢献、手法、結果、限界、実務的示唆、関連リンク（原著URL, data/code）。
- **自動支援:** 初回ドラフトはスクリプト（`research_bot.py`）で生成し、人がレビューして精査するワークフローを推奨。
- **タグ付けと内部リンク:** `tags:` と Obsidian の内部リンク `[[...]]` を必ず追加し、既存ノートとの接続を意図的に作る。

**3. 整理する（Organization）**
- **整理ツール:** 処理完了後、`inbox_organizer.py` を実行して処理済みファイルを `knowledge/archive/<source>/` に移動。
- **バージョン管理:** 研究ノートは Git 管理下でコミット。重要な更新には小さな履歴コミットを残す。
- **保守ルール:** 古いノートは3段階（active / reference / archive）で管理し、週次・月次でレビュー。

**運用上の推奨設定**
- **チェックリスト:** ノート作成テンプレート（ヘッダ・メタデータ・要約・引用）を用意。
- **スケジューリング:** Windows タスクスケジューラ／cron で収集スクリプトを実行。
- **監査ログ:** `knowledge/logs/inbox_sync.log` に取り込み・整理の履歴を残す。
- **品質ゲート:** 自動要約→人レビュー→承認→research 配備の3段階合意。

**短期アクション（推奨）**
- `inbox_organizer.py` の手動実行で現在の `inbox` を整理。
- `research_bot.py` の出力テンプレートを `knowledge/research/_templates/` に置き、レビュー手順を `README.md` として用意。

---

作成者: 自動要約（`SKILL.md` に基づく）
作成日: 2026-05-22
