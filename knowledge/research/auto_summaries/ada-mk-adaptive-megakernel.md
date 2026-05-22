---
title: ada-mk-adaptive-megakernel
authors: 
year: 
source: 
---

---
title: ada-mk-adaptive-megakernel
authors: 
year: 
source: 
---

---
title: ada-mk-adaptive-megakernel
authors: 
year: 
source: 
---

---
title: Ada-MK: Ada向けAdaptive MegaKernel最適化（LLM推論向け自動DAG探索）
authors: Wenxin Dong 他
year: 2026
source: knowledge/archive/academic_papers/Ada-MK__Adaptive_MegaKernel_Optimization_via_Automated_DAG-based_Search_for_LLM_Inference.md
tags: [高性能コンピューティング, LLM推論, GPU最適化]
---

概要:
LLM推論におけるカーネル起動オーバーヘッドと各オペレータ間のメモリアクセスコストを削減するためのMegaKernel技術を、NVIDIA Ada世代GPU向けに移植性と効率の両立を図る形で最適化したAda-MKを提案。コンパイル時に最適実行経路を確定することでランタイム分岐を排し、共有メモリ使用量削減やDAGベースのオフライン探索によって性能を改善する。

技術的貢献:
- 共有メモリ制約モデル（3次元）とK次元分割でピーク使用量を50%削減
- MLIRベースの詳細なDAGオフライン探索で最適実行経路を確定
- TensorRT-LLMへのプラグイン実装によるハイブリッド推論エンジン

結果:
- NVIDIA L20上で単一バッチスループットが最大23.6%向上（TensorRT-LLM比）、vLLM比で50.2%向上

示唆:
- 低レイテンシ環境（オンライン広告等）でのLLMデプロイにおいて、コンパイル時最適化を前提としたMegaKernel設計は有効。

制限:
- 固定したデプロイ構成を仮定するため、汎用的な動的ワークロードでは適用性が限定される可能性あり。

## 関連ファイル
- [[Ada-MK__Adaptive_MegaKernel_Optimization_via_Automated_DAG-based_Search_for_LLM_Inference]]
- [ソースファイル](../archive/academic_papers/Ada-MK__Adaptive_MegaKernel_Optimization_via_Automated_DAG-based_Search_for_LLM_Inference.md)
