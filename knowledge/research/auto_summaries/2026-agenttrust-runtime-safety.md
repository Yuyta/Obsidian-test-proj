---
title: 2026-agenttrust-runtime-safety
authors: 
year: 
source: 
---

---
title: 2026-agenttrust-runtime-safety
authors: 
year: 
source: 
---

---
title: 2026-agenttrust-runtime-safety
authors: 
year: 
source: 
---

---
title: AgentTrust: エージェントのツール利用におけるランタイム安全評価と介入
authors: Chen Yang
year: 2026
source: knowledge/archive/academic_papers/2026_AgentTrust Runtime Safety Evaluation and Intercep.md
tags: [AI-Agent, セキュリティ, ランタイム]
---

概要:
AIエージェントが実世界でツール呼び出しを行う際の危険を防ぐためのランタイム安全レイヤであるAgentTrustを提案。実行前にツール呼び出しを傍受し、allow/warn/block/reviewの判定を返す仕組みを備える。シェルの脱難読化、リスクチェーン検出、LLMを判定器として利用するキャッシュ対応などを組み合わせ、ベンチマークで高い判定精度を示す。

主な構成要素:
- シェル脱難読化ノーマライザ
- SafeFix（安全な代替案提示）
- RiskChain（多段攻撃チェーンの検出）
- キャッシュ対応LLM判定器（曖昧ケース）

評価:
- 300シナリオのベンチマークおよび追加の630シナリオで検証
- 生産ルールセットでの判定精度95.0%、リスクレベル精度73.7%（低ミリ秒のレイテンシ）

実装と公開:
- AGPL-3.0で公開、MCP互換のModel Context Protocolサーバを提供

示唆:
- エージェント運用において、実行前のコンテキスト理解と多段検査を組み合わせたランタイム防御は有効。

制限:
- 一部評価は内部ベンチマークに依存。実運用での長期評価が必要。

## 関連ファイル
- [[2026_AgentTrust Runtime Safety Evaluation and Intercep]]
- [ソースファイル](../archive/academic_papers/2026_AgentTrust Runtime Safety Evaluation and Intercep.md)
