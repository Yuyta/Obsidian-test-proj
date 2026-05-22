---
title: "Branch-Stochastic Model Predictive Control for Motion Planning under Multi-Modal Uncertainty with Scenario Clustering"
authors: ['Zekun Xing', 'Ramkrishna Chaudhari', 'Marion Leibold', 'Dirk Wollherr', 'Martin Buss']
published: 2026-05-21
arxiv_id: 2605.22600v1
url: https://arxiv.org/abs/2605.22600v1
---

Motion planning for autonomous driving must account for multi-modal uncertainty in both the intentions and trajectories of surrounding vehicles. Handling uncertainty in a worst-case manner guarantees robustness but often leads to excessive conservatism. Stochastic Model Predictive Control (SMPC) reduces trajectory-level conservatism through chance constraints, yet remains conservative with respect to intention uncertainty since constraints must hold across all intentions. We present a novel combination of SMPC and the branching structure, enabling the planner to generate distinct trajectories for different possible intentions while maintaining safety under trajectory uncertainty. A novel scenario clustering is proposed to merge prediction scenarios based on high-level decision similarity, thereby ensuring real-time tractability. Furthermore, an adaptive branching-time computation postpones commitment to separate plans until intention uncertainty is sufficiently reduced. Simulation studies in challenging highway scenarios demonstrate that the proposed method improves safety, reduces conservatism, and achieves real-time computational performance.
