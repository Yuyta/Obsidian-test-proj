---
title: 2026-the-two-boundaries-behavioral-ai-governance
authors: 
year: 
source: 
---

---
title: 2026-the-two-boundaries-behavioral-ai-governance
authors: 
year: 
source: 
---

---
title: The Two Boundaries: Why Behavioral AI Governance Fails Structurally
authors: Alan L. McCann
year: 2026
source: knowledge/inbox/academic_papers/2026_The Two Boundaries Why Behavioral AI Governance F.md
tags: [AI-governance, formal, security]
---

概要:
AIが現実世界で行う作用（API呼び出し、データ書込、ツール呼び出し等）に対するガバナンスが根本的に失敗する構造的理由を理論的に示す論考。表現可能性（what the system can do）とガバナンスが及ぶ範囲（what governance covers）の二つの境界を分離して定義し、その非一致がリスクと劇場（theater）を生むと主張する。

方法:
- 形式的枠組みの導入と、Riceの定理を用いた不可避性の議論（任意のチューリング完全な設計における意味的性質の判定不能性）
- Coterminous governance（表現可能性境界とガバナンス境界が一致する設計）を提案
- 証明はCoqで機械検証（454の定理、36モジュール）

主要主張:
- ガバナンスは単なる後付けレイヤでは限界があり、効果的なガバナンスにはシステムアーキテクチャレベルでの計算と効果の分離が必要
- Coterminous governance が設計原則となるべきで、これによりリスクと劇場の領域を消去できる可能性がある

示唆:
- 実用的ガバナンス設計は実行パイプラインに検査を組み込み、効果発生前にポリシーを適用するアーキテクチャ的決断を行うべき

制限:
- 理論的・形式的方法に基づく示唆が中心であり、実システムへの適用には工学的課題（性能、互換性）が残る。

## 関連ファイル
- [[2026_The Two Boundaries Why Behavioral AI Governance F]]
- [ソースファイル](../archive/academic_papers/2026_The Two Boundaries Why Behavioral AI Governance F.md)
