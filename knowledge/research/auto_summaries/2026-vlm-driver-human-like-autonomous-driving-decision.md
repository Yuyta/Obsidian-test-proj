---
title: 2026-vlm-driver-human-like-autonomous-driving-decision
authors: 
year: 
source: 
---

---
title: 2026-vlm-driver-human-like-autonomous-driving-decision
authors: 
year: 
source: 
---

---
title: 2026-vlm-driver-human-like-autonomous-driving-decision
authors: 
year: 
source: 
---

---
title: VLM-Driver: Human-Like Autonomous Driving Decision-Making via Vision Language Model
authors: Rui Zhao 他
year: 2026
source: knowledge/inbox/academic_papers/2026_VLM-Driver Human-Like Autonomous Driving Decision.md
tags: [autonomous-driving, VLM, decision-making]
---

概要:
VLMを用いて人間らしい運転意思決定を模倣するフレームワークを提案。全視野動画と複数ラウンドの質問応答に基づく段階的思考チェーンでグローバルな観察、行動計画、運動計画を統合する。AnyRes戦略やBilinear Interpolationによる特徴圧縮を導入し、計算コストと性能のバランスを最適化する。

方法:
- フルビュー動画を AnyRes で統一解像度化、ビジョンエンコーダで特徴抽出
- ビジョン特徴をテキスト埋め込み空間へ射影し、LLMバックボーンへ入力
- モーションヘッドで将来のウェイポイントを出力、意思決定特化の学習戦略を採用
- マルチモーダル運転指令データセットを新規構築して訓練

結果:
- シーン観察と行動計画で高い人間類似性を示し、運動計画の性能で既存手法を上回るSOTAを達成
- 未知の複雑シナリオに対する強い一般化性を報告

示唆:
- VLMによる段階的推論は解釈性と汎化性を両立しうる。自動運転の意思決定モジュール設計における新しい設計パターンを提示する。

制限:
- 提案手法はマルチモーダルデータと大規模モデルを前提とするため、実車組み込み時の計算・レイテンシ最適化が課題。

## 関連ファイル
- [[2026_VLM-Driver Human-Like Autonomous Driving Decision]]
- [ソースファイル](../archive/academic_papers/2026_VLM-Driver Human-Like Autonomous Driving Decision.md)
