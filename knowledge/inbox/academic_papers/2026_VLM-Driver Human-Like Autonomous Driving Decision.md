---
authors:
- Rui Zhao
- Qirui Yuan
- Jinyu Li
- Zhiqiang Wang
- Yun Li
- Zhenhai Gao
- Hongyu Hu
- Fei Gao
doi: 10.1109/TVT.2025.3629119
fetched_at: '2026-05-22 23:09:20'
status: Inbox
tags:
- paper
- automated-research
- autonomous-driving
title: 'VLM-Driver: Human-Like Autonomous Driving Decision-Making via Vision Language
  Model'
url: https://www.semanticscholar.org/paper/3b18503e52b5e2efd9751651a1457b74deb7a1cc
year: 2026
---



## Connections
- Topic: [[autonomous driving]]
- Type: [[Research Paper]]

## Abstract
Learning and simulating the decision processes of real-world human drivers is a key research direction in autonomous driving (AD). As the core of AD, existing decision systems typically face challenges in cross-scene generalization and decision interpretability: it requires understanding diverse dynamic driving scenarios and formulate transparent strategies that earn broad user trust. We propose VLM-Driver, a Vision-Language Model (VLM) framework with human-like chained driving decision thought, designed to progressively achieve global scene observation, high-level behavior planning, and low-level motion planning based on full-view driving videos, multi-round question queries and optional environmental perception information. Specifically, the full-view videos are resized to unified base resolution using the AnyRes strategy, and video features are extracted by a vision encoder. These video features are then mapped to the text embedding space via a vision-language projector and jointly fed into large language model (LLM) backbone with tokenized text embeddings. During this process, we introduce a Bilinear Interpolation method to efficiently compress the number of video features, ensuring an optimal balance between model performance and computational cost. Meanwhile, a dedicated motion head is designed to output refined future waypoints, improving the model's motion planning efficiency. Additionally, we construct a novel multimodal driving instruction dataset to support VLM-Driver training and introduce a decision-oriented training strategy to further enhance its chained reasoning capability. Extensive experiments show that VLM-Driver excels in scene observation and behavior planning, demonstrating high human-like consistency, and significantly outperforms existing baseline methods in motion planning, achieving SOTA performance. VLM-Driver also enable to handle unseen complex driving scenarios, exhibiting robust cross-scene generalization.