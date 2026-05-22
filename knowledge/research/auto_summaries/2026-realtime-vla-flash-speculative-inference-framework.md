---
title: 2026-realtime-vla-flash-speculative-inference-framework
authors: 
year: 
source: 
---

---
title: 2026-realtime-vla-flash-speculative-inference-framework
authors: 
year: 
source: 
---

---
title: 2026-realtime-vla-flash-speculative-inference-framework
authors: 
year: 
source: 
---

---
title: Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs
authors: Jiahui Niu 他
year: 2026
source: knowledge/inbox/academic_papers/2026_Realtime-VLA FLASH Speculative Inference Framewor.md
tags: [VLA, Inference, Latency]
---

概要:
Realtime-VLA FLASH は拡散型VLAのリアルタイム化を目的とした投機的推論フレームワーク。軽量なドラフトモデルで投機的に再計画を行い、主要モデルで並列検証し、必要時にフォールバックすることで多くの重い完全推論を回避する。

方法:
- ドラフトモデルによる投機的再計画
- メインモデルのAction Expertによる並列検証
- フェーズ依存のフォールバックメカニズム

結果:
- フル推論(58.0 ms)を投機(7.8 ms)で代替し、平均推論遅延を19.1 msへ短縮（3.04x）
- 実ロボットのベルトソート事例で有効性確認

示唆:
- 投機的手法はリアルタイム制約下でのdVLA適用を現実的にする。

制限:
- ドラフトと検証間の整合性保証やフォールバック頻度の制御が運用上重要。

## 関連ファイル
- [[2026_Realtime-VLA FLASH Speculative Inference Framewor]]
- [ソースファイル](../archive/academic_papers/2026_Realtime-VLA FLASH Speculative Inference Framewor.md)
