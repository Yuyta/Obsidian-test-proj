---
title: "Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping"
authors: ['Chouaib Bencheikh Lehocine', 'Adam Lilja', 'Junsheng Fu', 'Lars Hammarstrand']
published: 2026-05-21
arxiv_id: 2605.22578v1
url: https://arxiv.org/abs/2605.22578v1
---

Online map estimation is a crucial component of autonomous driving systems that reduces the reliance on costly high-definition maps. State-of-the-art (SOTA) methods commonly predict map elements as ordered sequences of points that form polylines and polygons. The evaluation of these methods relies predominantly on mean average precision (mAP) based on thresholded Chamfer distance (CD). This framework lacks sensitivity to point ordering and provides limited granularity in assessing geometric quality, making it difficult to distinguish which methods truly excel over others. In this work, we address these limitations on two fronts. For the single-instance similarity measure, we introduce sequence optimal sub-pattern assignment (SOSPA), an order-aware metric that enables fine-grained evaluation of individual geometries while satisfying all metric axioms. For the multi-instance evaluation framework, we propose polyline localisation and detection (PLD), a soft metric that jointly captures detection quality and geometric accuracy, replacing the hard thresholding of mAP with a principled soft assignment. Through evaluations on nuScenes, we demonstrate that PLD effectively ranks SOTA online mapping methods (MapTRv2, StreamMapNet, MapTracker) while providing a decomposed error analysis. This analysis identifies detection capability as the dominant bottleneck in current methods, revealing a performance trend that mAP fails to capture. Code for evaluation using our metrics will be released.
