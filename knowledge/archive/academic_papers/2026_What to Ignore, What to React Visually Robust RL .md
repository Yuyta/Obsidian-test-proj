---
authors:
- Yu Peng
- Jingjing Fu
- Chuheng Zhang
- Li Zhao
- Jiang Bian
- Mingyu Liu
- Ling Zhang
- Jun Zhang
- Rui Wang
doi: null
fetched_at: '2026-05-23 00:05:09'
status: Inbox
tags:
- paper
- automated-research
- VLA
title: 'What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models'
url: https://www.semanticscholar.org/paper/ca07518e255d5bbf71c58b351b4fa6aae03afacf
year: 2026
---



## Connections
- Topic: [[VLA]]
- Type: [[Research Paper]]

## Abstract
Reinforcement learning (RL) fine-tuning has shown promise for Vision-Language-Action (VLA) models in robotic manipulation, but deployment-time visual shifts pose practical challenges. A key difficulty is that standard task rewards supervise task success, but offer limited guidance on whether a visual change is task-irrelevant or changes the behavior required for manipulation. We propose PAIR-VLA (Paired Action Invariance&Sensitivity for Visually Robust VLA), an RL fine-tuning framework to address this difficulty by adding two auxiliary objectives over paired visual variants during PPO optimization: an invariance term that reduces the discrepancy between action distributions for a task-preserving pair (e.g., different distractors), and a sensitivity objective that encourages separable action distributions for a task-altering pair (e.g., target object in a different pose). Together, these objectives turn visual variants from mere observation diversity into behavior-level guidance on policy responses during RL fine-tuning. We evaluate on ManiSkill3 across two representative VLA architectures, OpenVLA and $\pi_{0.5}$, under diverse out-of-distribution visual shifts including unseen distractors, texture changes, target object pose variation, viewpoint shifts, and lighting changes. Our method consistently improves over standard PPO, achieving average improvements of 16.62% on $\pi_{0.5}$ and 9.10% on OpenVLA. Notably, ablations further show generalization across visual shifts: invariance guidance learned from distractor and texture variants transfers to target-pose and lighting shifts, while adding sensitivity guidance on target-pose variants further improves robustness to nuisance shifts, highlighting the broader transferability of behavior-level RL guidance.