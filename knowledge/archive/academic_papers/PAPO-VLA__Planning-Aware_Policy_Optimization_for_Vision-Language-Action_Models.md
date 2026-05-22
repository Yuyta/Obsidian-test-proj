---
title: "PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models"
authors: ['Peizheng Guo', 'Jingyao Wang', 'Changwen Zheng', 'Wenwen Qiang']
published: 2026-05-19
arxiv_id: 2605.19580v1
url: https://arxiv.org/abs/2605.19580v1
---

Vision-Language-Action (VLA) models show promising ability in language-guided robotic tasks. However, making VLA policies reliable remains challenging, because a manipulation task is completed through closed-loop interaction, where each action affects subsequent execution. To analyze this problem, we revisit VLA policy during execution and argue that a VLA policy acts both as a planner, which makes task-oriented decisions that change the direction of execution, and as an executor, which realizes these decisions through dense continuous actions. This view suggests that improving VLA reliability requires particular attention to planning actions. Existing optimization methods can imitate actions or improve complete trajectories, but they usually do not explicitly identify planning actions or measure their importance for task success. To address this issue, we propose Planning-Aware Policy Optimization for VLA models (PAPO-VLA). PAPO-VLA first identifies planning actions by jointly considering action variation and trajectory outcome, then estimates their importance through causal sufficiency and causal necessity, and finally incorporates this importance into GRPO advantage estimation. In this way, more important planning actions receive stronger optimization emphasis, while the whole trajectory is still optimized by trajectory-level feedback. Experiments on multiple benchmarks demonstrate the effectiveness of PAPO-VLA.
