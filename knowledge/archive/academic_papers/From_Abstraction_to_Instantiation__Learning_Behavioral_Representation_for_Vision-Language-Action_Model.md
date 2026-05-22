---
title: "From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model"
authors: ['Bing Hu', 'Zaijing Li', 'Rui Shao', 'Junda Chen', 'April Hua Liu', 'Wei-Shi Zheng', 'Liqiang Nie']
published: 2026-05-21
arxiv_id: 2605.22671v1
url: https://arxiv.org/abs/2605.22671v1
---

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (Avg.Len), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.
