---
title: "DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization"
authors: ['Sixu Lin', 'Yunpeng Qing', 'Litao Liu', 'Ming Zhou', 'Ruixing Jin', 'Xiaoyi Fan', 'Guiliang Liu']
published: 2026-05-17
arxiv_id: 2605.17486v1
url: https://arxiv.org/abs/2605.17486v1
---

Recent progress in Reinforcement Learning (RL) provides a principled approach to optimizing Vision-Language-Action (VLA) models, facilitating a shift from trajectory imitation to active learning in the task environment. Despite improvements in control precision, most RL optimizers remain task-specific, which reduces VLA models from generalist controllers to policies that overfit to a narrow set of tasks. In this study, we conduct an in-depth analysis of this phenomenon and highlight the importance of cross-task feature representations for improving the generalizability of VLA models. Motivated by this finding, we introduce DyGRO-VLA, a two-stage optimization framework that 1) effectively captures cross-task latent representations based on information-theoretic principles, and 2) dynamically refines policy optimization via a mixture-of-RL-residuals. DyGRO-VLA enables the RL optimizer to exploit task-relevant latent information while strategically mitigating adverse interference on the learned representations throughout the optimization process. We evaluate our approach on LIBERO, RoboTwin2 benchmarks, and further validate it on real world, demonstrating consistent improvements over strong baselines under multi-task training and distribution shift.
