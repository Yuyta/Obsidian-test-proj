---
title: "Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction"
authors: ['Henry Che', 'Jingkang Wang', 'Yun Chen', 'Ze Yang', 'Sivabalan Manivasagam', 'Raquel Urtasun']
published: 2026-05-21
arxiv_id: 2605.22420v1
url: https://arxiv.org/abs/2605.22420v1
---

Urban scene reconstruction from real-world observations has emerged as a powerful tool for self-driving development and testing. While current neural rendering approaches achieve high-fidelity rendering along the recorded trajectories, their quality degrades significantly under large viewpoint shifts, limiting the applicability for closed-loop simulation. Recent works have shown promising results in using diffusion models to enhance quality at these challenging viewpoints and distill improvements back into 3D representations. However, they often require costly per-scene optimization, and the distilled representations remain fragile and fail to generalize beyond limited synthesized views. To address these limitations, we propose GenRe, a novel diffusion-guided generalizable enhancer for urban scene reconstruction. GenRe takes as input any pretrained 3D Gaussian representation and fixes the deficiencies within a few minutes. By learning to distill generative priors across diverse scenes, GenRe produces robust and high-fidelity representation efficiently that generalizes reliably to challenging unseen viewpoints (e.g., lane change). Experiments show that GenRe outperforms existing methods in both quality and efficiency and benefits various downstream tasks, enabling robust and scalable sensor simulation for autonomous driving.
