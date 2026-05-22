---
title: "SCALE: Sensitivity-Aware Federated Unlearning with Information Freshness Optimization for Mobile Edge Computing"
authors: ['Zihao Ding', 'Beining Wu', 'Jun Huang']
published: 2026-05-21
arxiv_id: 2605.22589v1
url: https://arxiv.org/abs/2605.22589v1
---

Federated Unlearning (FU) is emerging as a powerful tool that enables the selective removal of client data to effectively address data contamination and meet strict privacy regulations in mobile edge computing (MEC) systems. Although FU has recently drawn attention in the AI community, existing approaches suffer from low unlearning precision and lack temporal information reflection, which results in suboptimal forgetting performance. To address these issues, we propose SCALE, a dual-level unlearning framework combining historical contribution analysis with information freshness-aware adaptive sparsification. Our framework first employs a historical contribution-based layer sensitivity analysis to identify layers most influenced by target clients, then performs fine-grained unlearning through adaptive sparsification at the weight sub-group level to balance information freshness with forgetting effectiveness. Through theoretical analysis, the proposed framework demonstrates the convergence properties and acceleration advantages. Our experiments and testbed results demonstrate superior unlearning effectiveness compared to state-of-the-art baselines, with significantly improved forgetting performance.
