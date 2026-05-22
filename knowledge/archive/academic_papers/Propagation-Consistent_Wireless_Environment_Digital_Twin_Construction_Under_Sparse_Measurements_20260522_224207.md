---
title: "Propagation-Consistent Wireless Environment Digital Twin Construction Under Sparse Measurements"
authors: ['Junjie Ai', 'Shurui Xu', 'Yanqing Ren', 'Zhuoyu Liu', 'Weicong Chen', 'Wankai Tang', 'Xiao Li', 'Chao-Kai Wen', 'Shi Jin']
published: 2026-05-21
arxiv_id: 2605.22361v1
url: https://arxiv.org/abs/2605.22361v1
---

Digital twins (DTs) are promising for wireless deployment, optimization, and data generation, but building a propagation-faithful twin from sparse real measurements remains difficult. This paper proposes a wireless environment digital twin (WEDT) construction paradigm that evolves a reconstructed geometric DT into a propagation-consistent wireless environment representation through calibration of a scene-level electromagnetic (EM) property field. Instead of directly fitting link-specific channel responses, the proposed paradigm first constructs a geometry-prior Bayesian channel map (BCM) to convert sparse position-labeled channel state information (CSI) into dense probabilistic supervision with uncertainty estimates. It then embeds the learnable EM property field into differentiable ray tracing (RT) based channel computation, thereby enabling calibration through an explicit propagation chain. Experiments in both public and real-world scenes show that WEDT achieves accurate channel prediction, generalizes to unseen transceiver topologies, and remains effective across different sampling conditions. WEDT also offers utility for material-related environment sensing, more reliable physical-layer planning, and higher-quality synthetic data generation for wireless AI. These results demonstrate the value of the proposed paradigm for propagation-consistent WEDT construction and related wireless applications.
