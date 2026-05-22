---
title: 2026-unisparsebev-multi-task-bev
authors: 
year: 
source: 
---

---
title: 2026-unisparsebev-multi-task-bev
authors: 
year: 
source: 
---

---
title: 2026-unisparsebev-multi-task-bev
authors: 
year: 
source: 
---

---
title: UniSparseBEV: A Multi-Task Learning Framework With Unified Sparse Query for Autonomous Driving
authors: Hao Zhou 他
year: 2026
source: knowledge/inbox/academic_papers/2026_UniSparseBEV A Multi-Task Learning Framework With.md
tags: [autonomous-driving, BEV, multi-task]
---

概要:
鳥瞰図(BEV)表現を用いた自動運転のマルチタスク学習において、密なBEV表現の計算負荷や構造複雑性を回避するため、共有学習可能クエリとZ軸Deformable Cross-Attention (Z-DCA) を導入した UniSparseBEV を提案する。2D監督の導入により学習効率も改善し、NuScenes上で3D検出・BEVセグメンテーションの複合タスクで既存手法を上回る。

方法:
- 共有の学習可能な sparse queries でタスク間情報交換を実現
- Z-DCA モジュールにより、BEVセグメンテーション用クエリが画像特徴から直接情報抽出
- 2D監督を組み込み学習効率を向上

結果:
- NuScenesでの広範評価で複数タスクでの性能向上と堅牢性を示す

示唆:
- 密なBEVを使わないSparseクエリ設計は計算効率とマルチタスク性の両立に有効であり、実装コストを下げつつ推論品質を維持できる。

制限:
- 実車条件や極端なセンサ欠損下での堅牢性評価が今後の課題。

## 関連ファイル
- [[2026_UniSparseBEV A Multi-Task Learning Framework With]]
- [ソースファイル](../archive/academic_papers/2026_UniSparseBEV A Multi-Task Learning Framework With.md)
