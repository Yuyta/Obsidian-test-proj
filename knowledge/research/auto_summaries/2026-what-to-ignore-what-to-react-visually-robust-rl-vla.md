---
title: 2026-what-to-ignore-what-to-react-visually-robust-rl-vla
authors: 
year: 
source: 
---

---
title: 2026-what-to-ignore-what-to-react-visually-robust-rl-vla
authors: 
year: 
source: 
---

---
title: What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models
authors: Yu Peng 他
year: 2026
source: knowledge/inbox/academic_papers/2026_What to Ignore, What to React Visually Robust RL .md
tags: [VLA, RL, robustness]
---

概要:
VLAモデルのRL微調整における視覚的な分布ずれ（distractors, texture, pose, lighting等）に対処するため、PAIR-VLAという二重目的（invarianceとsensitivity）を導入した強化学習フレームワークを提案。ペア化された視覚変換に対して行動分布の不変性と感度を同時に学習させることで、視覚的摂動に対する行動レベルの頑健性を獲得する。

方法:
- PAIR-VLA: PPOベースの最適化に2つの補助損失を追加
  - Invariance: タスク保存的ペア間で行動分布の差を縮小
  - Sensitivity: タスクを変更するペア間で行動分布の分離を促進
- 評価: ManiSkill3 上で OpenVLA と π_{0.5} の2種構成で、複数の視覚シフトを横断評価

主要結果:
- π_{0.5} で平均改善16.62%、OpenVLAで9.10%の性能向上を達成
- 抽出実験により、雑音/テクスチャ由来の不変性は姿勢や照明への一般化を示し、感度損失を組み合わせることで目標ポーズ変化への堅牢性がさらに改善されることを確認

示唆:
- 視覚変動を単なる観察多様性とせず、行動レベルの学習信号に変換することは実用的かつ転移性の高い堅牢化手法である。

制限:
- 評価は ManiSkill3 と限定アーキテクチャに依存。異機種ロボットでのさらなる検証が必要。

## 関連ファイル
- [[2026_What to Ignore, What to React Visually Robust RL ]]
- [ソースファイル](../archive/academic_papers/2026_What to Ignore, What to React Visually Robust RL .md)
