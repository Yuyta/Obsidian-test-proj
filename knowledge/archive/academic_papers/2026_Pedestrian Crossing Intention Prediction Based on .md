---
authors:
- Chenxi Lin
- Xiaojian Hu
doi: 10.1109/TITS.2026.3654084
fetched_at: '2026-05-22 23:09:20'
status: Inbox
tags:
- paper
- automated-research
- autonomous-driving
title: Pedestrian Crossing Intention Prediction Based on Cross-Modal Motion Query
  and Global–Local Context Co-Learning for Autonomous Driving
url: https://www.semanticscholar.org/paper/cafe0d76f9ea3382da6f5c301257e9321c9f8ff5
year: 2026
---



## Connections
- Topic: [[autonomous driving]]
- Type: [[Research Paper]]

## Abstract
Ensuring safety in autonomous driving requires accurate pedestrian intention prediction in complex urban environments. Nevertheless, pedestrian motion is inherently influenced by environmental factors and visual appearance, which poses a significant challenge. Although existing multi-modal methods integrate motion data with both global and local visual cues during training, applying the same model structure for inference results in high computational cost and reduces real-time performance. To address this limitation, we propose the Global-Local Context Co-learning (GLCCL) framework, which leverages both local and global context during training for collaborative learning while relying solely on lightweight motion data for efficient real-time inference. Our framework integrates three key components: a Cross-modal Query Module (CQM) for modeling vehicle-pedestrian motion feature, a Local Perception Module (LPM) for extracting local pedestrian features, and a Global Guidance Module (GGM) for encoding global traffic environment descriptions. Collaboratively training these modules enables our framework to enrich motion representations with global-local contextual information. We further visualize the CQM’s cross-attention matrices to interpret the interactions of multi-modal motion features. Experiments on the public PIE and JAAD benchmarks demonstrate that, compared with state-of-the-art multi-modal models, GLCCL achieves competitive performance while offering superior real-time capabilities and lower computational cost. Extensive ablation studies confirm the framework’s compatibility with diverse sequence-learning methods.