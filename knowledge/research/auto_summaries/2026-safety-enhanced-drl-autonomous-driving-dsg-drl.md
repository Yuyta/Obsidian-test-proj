---
title: 2026-safety-enhanced-drl-autonomous-driving-dsg-drl
authors: 
year: 
source: 
---

---
title: 2026-safety-enhanced-drl-autonomous-driving-dsg-drl
authors: 
year: 
source: 
---

---
title: Safety-Enhanced Deep Reinforcement Learning for Autonomous Driving: DSG-DRL
authors: Zhuoren Li 他
year: 2026
source: knowledge/inbox/academic_papers/2026_Safety-Enhanced Deep Reinforcement Learning for Au.md
tags: [autonomous-driving, DRL, safety]
---

概要:
レーンチェンジなどの運動計画タスクにおいて、危険行動を敢えて経験させることでより安全で高速に学習する動的安全ガイダンス（DSG-DRL）を提案する。危険な挙動を強調して記憶バッチとサンプリング優先度を調整し、トレーニングとテスト時に動的制約を課すことで安全性と学習速度を向上させる。

方法:
- 危険挙動を評価するリスク予測器を用い、その体験を増強して学習データに反映
- 優先サンプリングと追加メモリバッチによる危険事例学習の強化
- 学習中・テスト中に動的制約を課すことで無謀な行動を抑制

結果:
- シミュレーション検証で、従来DRL手法よりも高速な収束と高い安全性能を示す
- 高い安全性を確保しつつ運転効率を維持することを報告

示唆:
- 危険事例を学習資源として積極的に活用する戦略は、安全性が重視される自動運転学習に有効

制限:
- 現在の検証はシミュレーション中心。実車環境での安全検証とパラメータ調整が必要。

## 関連ファイル
- [[2026_Safety-Enhanced Deep Reinforcement Learning for Au]]
- [ソースファイル](../archive/academic_papers/2026_Safety-Enhanced Deep Reinforcement Learning for Au.md)
