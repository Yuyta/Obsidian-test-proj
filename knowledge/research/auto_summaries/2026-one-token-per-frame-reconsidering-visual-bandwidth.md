---
title: 2026-one-token-per-frame-reconsidering-visual-bandwidth
authors: 
year: 
source: 
---

---
title: 2026-one-token-per-frame-reconsidering-visual-bandwidth
authors: 
year: 
source: 
---

---
title: 2026-one-token-per-frame-reconsidering-visual-bandwidth
authors: 
year: 
source: 
---

---
title: One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy
authors: Mark Tang 他
year: 2026
source: knowledge/inbox/academic_papers/2026_One Token Per Frame Reconsidering Visual Bandwidt.md
tags: [VLA, World-Model, Representation]
---

概要:
OneWM-VLA を提案。各フレームを1つの意味トークンに圧縮することで視覚帯域を大幅に削減し、フロー・マッチングで潜在ストリームと行動軌道を同時に生成する。追加のLoRA微調整で複数ベンチマーク（MetaWorld MT50, LIBERO-Long, Fold Cloth）で大幅改善を示した。

方法:
- Adaptive Attention Pooling によるフレーム圧縮（1トークン/フレーム）
- 単一の flow-matching 目的で潜在ストリームと行動を同時推論
- LoRA 微調整（14.71Mパラメータ）

結果:
- MetaWorld MT50: 成功率47.9% → 61.3%
- LIBERO-Long: 95.6%（vs 85.2%）
- Fold Cloth（実ロボット）: 60.0%（vs 20.0%）

示唆:
- フレームごとの視覚情報を大幅に圧縮しても長期計画性能を維持でき、伝送・推論コストの削減に有効。

制限:
- 事前学習バックボーンやLoRA設定依存の結果。実世界一般化は追加検証が必要。

## 関連ファイル
- [[2026_One Token Per Frame Reconsidering Visual Bandwidt]]
- [ソースファイル](../archive/academic_papers/2026_One Token Per Frame Reconsidering Visual Bandwidt.md)
