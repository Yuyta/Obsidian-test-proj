---
title: "N3P: Accelerated Automated Parking via a Learning-Based Naturalistic Three-Stage Scheme"
authors: ['Yifan Xue', 'Toktam Mohammadnejad', 'Faizan M Tariq', 'Sangjae Bae', 'David Isele', 'Yosuke Sakamoto', 'Nadia Figueroa', "Jovin D'sa"]
published: 2026-05-21
arxiv_id: 2605.22722v1
url: https://arxiv.org/abs/2605.22722v1
---

Autonomous parking requires efficient path planning that ensures kinematic feasibility and collision avoidance in constrained environments. Hybrid A* is widely used but computationally expensive, while reinforcement learning (RL) methods lack reliability and often struggle with long-horizon geometric constraints, leading to suboptimal trajectories. We present N3P, a fast learning-based three-stage framework for automated parking. By introducing an intermediate preparatory pose and using a learning module to predict it, N3P decomposes the maneuver into simpler subproblems, thereby reducing computational complexity and accelerating path generation. We validate the framework by integrating it with Hybrid A* algorithms. Experiments in perpendicular and parallel parking scenarios show that N3P-enhanced Hybrid A* speeds up planning by more than 80%. It also outperforms RL baselines in success rate and trajectory quality, producing shorter trajectories with fewer gear changes, while achieving comparable or lower planning time in most cases.
