---
title: "Vision-Language-Action (VLA) Models Latest Trends (2024-2025)"
authors: ["Antigravity Research Agent"]
year: 2025
doi: null
url: null
status: "Inbox"
tags: ["paper", "robotics", "VLA", "AI-Agent", "DeepLearning"]
fetched_at: '2026-05-09 22:16:00'
---

## Connections
- Topic: [[VLA]]
- Related: [[Vision Language Model]], [[Physical AI]], [[Robotics]], [[Foundation Models]], [[Embodied AI]]
- Key Frameworks: [[OpenVLA]], [[RT-2]], [[Project GR00T]]

---

## 1. 主要なモデル（Major Models）

### **OpenVLA (2024-2025)**
- **概要**: 70億パラメータ（7B）を持つ最先端のオープンソースVLAモデル。
- **特徴**: Prismatic VLM（DINOv2 + SigLIP + Llama 2）をベースに、97万件のロボット操作データでファインチューニング。
- **独自性**: 既存の商用モデル（RT-2など）に匹敵する性能を、家庭用GPUでも推論可能なサイズで実現している。
- **GitHub**: [openvla/openvla](https://github.com/openvla/openvla)

### **RT-2 / RT-2-X (Google DeepMind)**
- **概要**: PaLM-EおよびViTを基盤とした巨大なVLAモデル（最大55B）。
- **特徴**: ロボットのアクション（制御命令）をテキストトークンとして直接出力する「Action-as-Text」アプローチを採用。
- **独自性**: チェーン・オブ-ソート（思考の連鎖）を用いることで、複雑な推論を伴うロボット操作（例：「壊れやすい物を避けて片付けて」）が可能。

### **Project GR00T (NVIDIA, 2025)**
- **概要**: ヒューマノイド（人型ロボット）向けの汎用基盤モデル。
- **特徴**: マルチモーダル入力（視覚・言語・モーション）を受け取り、全身制御を行う。
- **独自性**: シミュレーション（Isaac Lab）と実データのハイブリッド学習により、人間のような自然な動きを実現。

---

## 2. 使用されているデータセット（Datasets）

### **Open X-Embodiment**
- **概要**: 「ロボット界のImageNet」と呼ばれる世界最大級のデータセット。
- **規模**: 22種類以上のロボットプラットフォーム、500以上のスキル、100万件以上の軌跡データ。
- **重要性**: 異なる形状のロボット（多脚、アーム、ヒューマノイド）間で知識を共有する「Cross-Embodiment」学習を可能にしている。
- **GitHub**: [google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)

---

## 3. 現在の課題と将来の方向性

### **主な課題（Current Challenges）**
- **推論速度（Latency）**: VLAは計算量が多いため、リアルタイム制御に必要な高周波（10Hz以上）での動作が困難。
- **データの希少性**: 実世界のデータ収集はコストが高く、シミュレーションと現実のギャップ（Sim-to-Real）の解消が不可欠。
- **未知環境への適応性**: 学習データに含まれない新しい物体や環境（Out-of-Distribution）での信頼性向上。

### **将来の方向性（Future Directions）**
- **階層型VLA (RT-H)**: 複雑なタスクを言語的なサブゴールに分割して処理する構造。
- **効率的な推論技術 (VLA-Cache)**: 適応的なトークンキャッシングなどによる高速化。

---
### 分析のまとめ
VLAモデルは、2024年の **OpenVLA** の登場によりオープンソース化が加速し、2025年にはNVIDIAの **GR00T** に代表されるヒューマノイドへの特化や、リアルタイム性を重視した軽量モデルへのシフトが見られます。Obsidianのグラフビューでは、[[OpenVLA]] や [[Open X-Embodiment]]をハブとして、関連する論文や実装を繋げていくことで、分野全体の構造を可視化できます。
