---
title: "Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs"
authors: ['Jiahui Niu', 'Kefan Gu', 'Yucheng Zhao', 'Shengwen Liang', 'Tiancai Wang', 'Xing Hu', 'Ying Wang', 'Huawei Li']
published: 2026-05-13
arxiv_id: 2605.13778v1
url: https://arxiv.org/abs/2605.13778v1
---

Diffusion-based vision-language-action models (dVLAs) are promising for embodied intelligence but are fundamentally limited in real-time deployment by the high latency of full inference. We propose Realtime-VLA FLASH, a speculative inference framework that eliminates most full inference calls during replanning by introducing a lightweight draft model with parallel verification via the main model's Action Expert and a phase-aware fallback mechanism that reverts to the full inference pipeline when needed. This design enables low-latency, high-frequency replanning without sacrificing reliability. Experiments show that on LIBERO, FLASH largely preserves task performance by replacing many 58.0 ms full-inference rounds with speculative rounds as fast as 7.8 ms, lowering task-level average inference latency to 19.1 ms (3.04x speedup). We additionally demonstrate effectiveness on real-world conveyor-belt sorting, highlighting its practical impact for latency-critical embodied tasks.
