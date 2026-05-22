---
title: 2026-onewm-vla-one-token-per-frame
authors: 
year: 
source: 
---

---
title: 2026-onewm-vla-one-token-per-frame
authors: 
year: 
source: 
---

---
title: OneWM-VLA: One Token Per Frame for World Models in VLA Policies
authors: Mark Tang 他
year: 2026
source: knowledge/inbox/academic_papers/2026_One Token Per Frame Reconsidering Visual Bandwidt.md
tags: [VLA, World-Model, Representation]
---

概要:
OneWM-VLA は各フレームを1つの意味トークンに圧縮する表現設計を導入し、フロー・マッチングによって潜在ストリームと行動軌道を同時に生成する。Frozen backbone 上での LoRA 微調整により複数ベンチマークで性能を大幅に改善した。

主要結果:
- MetaWorld MT50: 47.9% → 61.3%
- LIBERO-Long: 95.6%（改善）
- Fold Cloth（実ロボ）: 60.0%（改善）

実用的示唆:
- 視覚帯域を大幅に削減しても長期計画性能を維持できるため、通信・推論コストを削減しつつ実ロボット適用が可能。

## 関連ファイル
- [[2026_One Token Per Frame Reconsidering Visual Bandwidt]]
- [ソースファイル](../archive/academic_papers/2026_One Token Per Frame Reconsidering Visual Bandwidt.md)
