---
title: 2026-why-are-agentic-pull-requests-merged-or-rejected
authors: 
year: 
source: 
---

---
title: 2026-why-are-agentic-pull-requests-merged-or-rejected
authors: 
year: 
source: 
---

---
title: 2026-why-are-agentic-pull-requests-merged-or-rejected
authors: 
year: 
source: 
---

---
title: Why Are Agentic Pull Requests Merged or Rejected? An Empirical Study
authors: Sien Reeve O. Peralta 他
year: 2026
source: knowledge/inbox/academic_papers/Why_Are_Agentic_Pull_Requests_Merged_or_Rejected__An_Empirical_Study_20260522_224207.md
tags: [agentic-pr, empirical, software-engineering]
---

概要:
エージェント型コード生成ツールが提出するPR（Agentic-PR）のマージ/拒否結果だけでエージェント性能を評価するのは不十分であることを示す大規模実証研究。11,048件のクローズ済PRから9,799件の人間レビューPRを抽出し、代表717件を手動解析してレビュー過程のアーティファクトから意思決定理由を再構成した。

方法:
- データ: 11,048件のAgentic-PR（精査後9,799件）から代表サンプル717件を手動コードブックでコーディング
- 分析: 出力ラベル（merged/rejected）とレビューインタラクションの関係を定量・定性混合で解析

主要所見:
- 拒否(PR rejected)のうち実際にエージェントの明確な失敗と判定できるのは35.7%に過ぎない。
- 31.2%はワークフロー制約（タイミング、既存方針等）が原因で、33.1%は判断理由が観測できない。
- マージされたPRのうち15.4%はレビュアーの手作業（フィードバックや直接コミット）を経ており、5.5%はレビュー痕跡がない。
- エージェント毎の振る舞い差も明確で、CopilotやDevinはレビュアー介入型ワークフローで運用されることが多く、CodexやCursorは最小の介入でマージされる傾向があった。

示唆:
- PRアウトカム単独での評価は誤解を招くため、レビューインタラクションを含めた“インタラクション認識評価”が必要。
- エージェントの運用設計（レビューワークフロー）を測定に組み込むべきで、ベンチマーク設計にも反映されるべきである。

制限:
- 手動解析は代表サンプルに依存するため外挿の注意。公開データのみでは内部意図や非公開方針が欠落する。

## 関連ファイル
- [[Why_Are_Agentic_Pull_Requests_Merged_or_Rejected__An_Empirical_Study_20260522_224207]]
- [ソースファイル](../archive/academic_papers/Why_Are_Agentic_Pull_Requests_Merged_or_Rejected__An_Empirical_Study_20260522_224207.md)
