# 運用

inboxフォルダを定期的にチェックし、自律的に以下の「収集・昇華・整理」の知識管理サイクルを回す。

## 1. 収集フェーズ (Collection)
*   定期的に（または起動時に）、`research_bot.py` や `youtube_summarizer.py` に加え、`arxiv_research_bot.py` などの収集スクリプトを実行し、最新の論文や市場動向を `knowledge/inbox/` 内の各フォルダに集約する。

## 2. 昇華フェーズ (Synthesis & Refinement)
*   `knowledge/inbox/` に溜まった生データを分析し、既存知識と結びつけながら `knowledge/research/` の適切なカテゴリ（例: `mlops`, `robotics`, `ai-agent` 等）に構造化された調査成果物（統合メモ）として作成・更新する。
*   既存の `research/` フォルダ内の内容が古くなっている場合は、`inbox/` の新しい情報に基づいて上書きまたは追記（情報の更新）を行う。
*   Obsidianの特性を活かし、タグ（`tags`）や内部リンク（`[[Note Name]]`）を付与して情報の検索性とグラフの接続性を向上させる。

## 3. 整理フェーズ (Organization)
*   成果物の作成・統合が完了した後、必ず `inbox_organizer.py` を実行する。
*   `inbox/` 内の処理済みファイルを、元の情報源が判別できるように `knowledge/archive/<情報源>/` 配下に移動し、`inbox/` 内をクリーンに保つ。

# 運用する上での検討事項

*   synthesisに情報を格納する際は、他のフォルダとどう使い分けるか、また各フォルダどれくらいの粒度の情報を格納すべきか。