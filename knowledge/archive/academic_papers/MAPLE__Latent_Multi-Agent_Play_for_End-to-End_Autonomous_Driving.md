---
title: "MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving"
authors: ['Rajeev Yasarla', 'Deepti Hegde', 'Hsin-Pai Cheng', 'Shizhong Han', 'Yunxiao Shi', 'Meysam Sadeghigooghari', 'Hanno Ackermann', 'Litian Liu', 'Pranav Desai', 'Fatih Porikli', 'Mohammad Ghavamzadeh', 'Hong Cai']
published: 2026-05-13
arxiv_id: 2605.14201v2
url: https://arxiv.org/abs/2605.14201v2
---

Vision-language-action (VLA) models are effective as end-to-end motion planners, but can be brittle when evaluated in closed-loop settings due to being trained under traditional imitation learning framework. Existing closed-loop supervision approaches lack scalability and fail to completely model a reactive environment. We propose MAPLE, a novel framework for reactive, multi-agent rollout of a dynamic driving scenario in the latent space of the VLA model. The ego vehicle and nearby traffic agents are independently controlled over multi-step horizons, while being reactive to other agents in the scene, enabling closed-loop training. MAPLE consists of two training stages: (1) supervised fine-tuning on the latent rollouts based on ground-truth trajectories, followed by (2) reinforcement learning with global and agent -specific rewards that encourage safety, progress, and interaction realism. We further propose diversity rewards that encourage the model to generate planning behaviors that may not be present in logged driving data. Notably, our closed-loop training framework is scalable and does not require external simulators, which can be computationally expensive to run and have limited visual fidelity to the real-world. MAPLE achieves state-of-the-art driving performance on Bench2Drive and demonstrates scalable, closed-loop multi-agent play for robust E2E autonomous driving systems.
