---
authors:
- Yuzhou Huang
- Benjin Zhu
- Hengtong Lu
- Victor Shea-Jay Huang
- Haiming Zhang
- Wei Chen
- Jifeng Dai
- Yangjiang Xie
- Hongsheng Li
doi: null
fetched_at: '2026-05-22 23:09:20'
status: Inbox
tags:
- paper
- automated-research
- autonomous-driving
title: 'MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous
  Driving'
url: https://www.semanticscholar.org/paper/b9578e45ee4af3502bcfa63a56b93c90121a5886
year: 2026
---



## Connections
- Topic: [[autonomous driving]]
- Type: [[Research Paper]]

## Abstract
Autonomous driving has progressed from modular pipelines toward end-to-end unification, and Vision-Language-Action (VLA) models are a natural extension of this journey beyond Vision-to-Action (VA). In practice, driving VLAs have often trailed VA on planning quality, suggesting that the difficulty is not simply model scale but the interface through which semantic reasoning, temporal context, and continuous control are combined. We argue that this gap reflects how VLA has been built -- as isolated subtask improvements that fail to compose into coherent driving capabilities -- rather than what VLA is. We present MindVLA-U1, the first unified streaming VLA architecture for autonomous driving. A unified VLM backbone produces autoregressive language tokens and flow-matching continuous action trajectories in a single forward pass over one shared representation, preserving the natural output form of each modality. A streaming design processes the driving video framewise rather than as fixed video-action chunks, while a learned memory channel carries temporal context across frames so planned trajectories evolve smoothly without redundant multi-frame VLM modeling. The unified architecture admits fast/slow execution on dense/sparse Mixture-of-Transformers (MoT) backbones via flexible self-attention context management, and exposes a measurable language-to-action route: a language-predicted driving intent steers action diffusion through classifier-free guidance (CFG), turning language-side intent into a control signal for continuous trajectory generation. On the long-tail WOD-E2E benchmark, MindVLA-U1 surpasses experienced human drivers for the first time (8.20 RFS vs. 8.13 GT RFS) with 2 diffusion steps, achieves state-of-the-art planning ADEs over prior VA/VLA methods by large margins, and matches VA-class throughput (16 FPS vs. RAP-DINO's 18 FPS) while preserving natural-language interfaces.