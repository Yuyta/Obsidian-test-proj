---
title: "Ada-Diffuser: Latent-Aware Adaptive Diffusion for Decision-Making"
authors: ['Fan Feng', 'Selena Ge', 'Minghao Fu', 'Zijian Li', 'Yujia Zheng', 'Zeyu Tang', 'Yingyao Hu', 'Biwei Huang', 'Kun Zhang']
published: 2026-05-15
arxiv_id: 2605.16054v1
url: https://arxiv.org/abs/2605.16054v1
---

Recent work has framed decision-making as a sequence modeling problem using generative models such as diffusion models. Although promising, these approaches often overlook latent factors that exhibit evolving dynamics, elements that are fundamental to environment transitions, reward structures, and high-level agent behavior. Explicitly modeling these hidden processes is essential for both precise dynamics modeling and effective decision-making. In this paper, we propose a unified framework that explicitly incorporates latent dynamic inference into generative decision-making from minimal yet sufficient observations. We theoretically show that under mild conditions, the latent process can be identified from small temporal blocks of observations. Building on this insight, we introduce Ada-Diffuser, a causal diffusion model that learns the temporal structure of observed interactions and the underlying latent dynamics simultaneously, and furthermore, leverages them for planning and control. With a modular design, Ada-Diffuser supports both planning and policy learning tasks, enabling adaptation to latent variations in dynamics, rewards, and latent actions. Experiments on simulated control and robotic benchmarks demonstrate its effectiveness in accurate latent inference and adaptive policy learning.
