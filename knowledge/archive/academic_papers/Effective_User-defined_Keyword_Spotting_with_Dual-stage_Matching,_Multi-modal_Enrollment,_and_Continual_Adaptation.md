---
title: "Effective User-defined Keyword Spotting with Dual-stage Matching, Multi-modal Enrollment, and Continual Adaptation"
authors: ['Zhiqi Ai', 'Han Cheng', 'Shiyi Mu', 'Xinnuo Li', 'Yongjin Zhou', 'Shugong Xu']
published: 2026-05-21
arxiv_id: 2605.22120v1
url: https://arxiv.org/abs/2605.22120v1
---

User-defined keyword spotting (KWS) is crucial for personalized voice interaction, yet existing methods face several challenges: (1) insufficient discriminability among confusable words, (2) performance inconsistency across speakers with varying pronunciations, and (3) high data cost to ensure reliable wake-word performance. In this paper, we introduce DMA-KWS, an efficient and robust framework for user-defined keyword spotting. First, it adopts a dual-stage matching pipeline: CTC decoding with streaming phoneme search to locate candidate segments, followed by QbyT with a phoneme matcher for fine-grained verification, enabling it to better distinguish confusable words. Next, multi-modal enrollment fuses user-specific speech with text embeddings to further improve accuracy for registered users. Finally, a parameter-efficient continual adaptation mechanism performs lightweight updates using synthetic and real data. Extensive experiments demonstrate the superior performance of DMA-KWS. On the LibriPhrase Hard subset, it achieves 97.85% AUC and 6.13% EER, reaching state-of-the-art performance. In speaker-dependent settings, DMA-KWS consistently outperforms text-only enrollment, demonstrating significant performance gains. Moreover, the proposed parameter-efficient fine-tuning mechanism adapts DMA-KWS with only 187k updated parameters, further enhancing KWS performance while ensuring suitability for on-device deployment.
