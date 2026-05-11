# VLA・ヒューマノイド研究動向

## 1. VLA (Vision-Language-Action) モデルの進化

### 主要モデル
- **OpenVLA (2024-2025)**: 7Bパラメータのオープンソースモデル。Prismatic VLMベースで、家庭用GPUでの推論が可能。
- **RT-2 / RT-2-X (Google DeepMind)**: 「Action-as-Text」アプローチを採用し、PaLM-Eを基盤とした巨大モデル。思考の連鎖（CoT）による複雑な推論が可能。
- **Project GR00T (NVIDIA, 2025)**: ヒューマノイド向けの全身制御基盤モデル。Isaac Labによるシミュレーションと実データのハイブリッド学習。

### 基盤データセット
- **Open X-Embodiment**: 「ロボット界のImageNet」。22種類以上のプラットフォーム、100万件以上の軌跡データを統合。

## 2. ヒューマノイドの量産化
- **フェーズの変化**: 「研究・PoC」から「量産（Annual 10k+ units）」へ。
- **主要プレイヤー**:
    - **Hyundai + Boston Dynamics**: 2028年までに年3万台量産体制。
    - **Tesla Optimus**: 工場自動化および家庭向け展開。
    - **中国勢 (Agibot, Unitree, UBTECH)**: サプライチェーンの強みを活かした低コスト量産。

## 3. 技術的課題とトレンド
- **Latency（推論速度）**: リアルタイム制御に必要な高周波（10Hz以上）動作への対応。
- **Sim-to-Real**: シミュレーションと現実のギャップ解消。
- **Physical Reasoning**: 物理法則に基づいた推論と、安全性の担保（Safety Alignment）。

## 4. 関連キーワード
- [[VLA]]
- [[Embodied AI]]
- [[World Model]]
- [[Foundation Models for Robotics]]
