---
authors:
- Mark Tang
- Shengchao Yuan
- Xiaoxin Bai
- Zhi Jin
- De Ma
- Gang Pan
- Bing Liu
doi: null
fetched_at: '2026-05-23 00:05:09'
status: Inbox
tags:
- paper
- automated-research
- VLA
title: 'One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA
  Policy'
url: https://www.semanticscholar.org/paper/322e5b81345cb725834764069edb48d768d9f4e2
year: 2026
---



## Connections
- Topic: [[VLA]]
- Type: [[Research Paper]]

## Abstract
Vision-language-action (VLA) models increasingly rely on auxiliary world modules to plan over long horizons, yet how such modules should be parameterized on top of a pretrained VLA remains an open design question. Existing world-model-augmented VLAs typically pass the per-frame visual stream into the world module at high visual bandwidth and treat its rollout as a side product of action prediction; under a constrained adaptation budget on a frozen backbone, this leaves both the per-frame representation and the latent action coupling under-examined. We introduce OneWM-VLA, which compresses each view into a single semantic token per frame through an Adaptive Attention Pooling, and produces the resulting latent stream and the action trajectory under a single flow-matching objective rather than connecting them through a separate decoder. Empirically, we find that per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance under our setup. Trained with 14.71M LoRA parameters on a $\pi_0$ (2B) backbone, OneWM-VLA improves the average success rate from 47.9% to 61.3% on MetaWorld~MT50, reaches 95.6% on LIBERO-Long (vs.85.2% for $\pi_0$), and reaches 60.0% on the long-horizon deformable task Fold Cloth on a real Piper arm (vs.20.0% for $\pi_0$).