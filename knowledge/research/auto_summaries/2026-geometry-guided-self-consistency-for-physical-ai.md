---
title: 2026-geometry-guided-self-consistency-for-physical-ai
authors: 
year: 
source: 
---

---
title: 2026-geometry-guided-self-consistency-for-physical-ai
authors: 
year: 
source: 
---

---
title: Geometry Guided Self-Consistency for Physical AI
authors: Yinwei Dai, Zhuofu Chen, Lijie Yang, Ravi Netravali
year: 2026
source: knowledge/inbox/academic_papers/2026_Geometry Guided Self-Consistency for Physical AI.md
tags: [Physical-AI, VLA, Inference]
---

概要:
KeyStone と名付けられた、拡散/フローマッチングベースの行動生成に対する推論時の自己一貫性手法を提案する。複数の候補アクションチャンクを並列に生成し、連続空間でクラスタリングして最大クラスターのメドイドを返すことで、単一軌道サンプリングの脆弱性を軽減する。追加学習は不要で、タスク成功率を最大13.3%向上させる。

方法:
- 推論時にK個の候補チャンクを並列生成
- 連続行動空間でクラスタリングし、最大クラスターのメドイドを選択
- 追加モデル学習は不要（判定器を必要としない）

主な結果:
- さまざまなVLAやWAMで成功率が最大13.3%向上
- レイテンシ影響はほぼ無視できる（並列生成の計算リソース余裕を利用）

示唆:
- 推論時の多様性を利用した選択は、物理行動空間の幾何構造により有効で、実ロボット運用での堅牢性向上に寄与する。

制限:
- チャンクサイズやKの選択が性能に依存。大規模実装でのリソース配分評価が必要。

## 関連ファイル
- [[2026_Geometry Guided Self-Consistency for Physical AI]]
- [ソースファイル](../archive/academic_papers/2026_Geometry Guided Self-Consistency for Physical AI.md)
