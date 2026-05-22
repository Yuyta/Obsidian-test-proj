---
title: "Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action"
authors: ['Pengteng Li', 'Weiyu Guo', 'He Zhang', 'Tiefu Cai', 'Xiao He', 'Yandong Guo', 'Hui Xiong']
published: 2026-05-21
arxiv_id: 2605.22283v1
url: https://arxiv.org/abs/2605.22283v1
---

We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models. Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera's field of view. SOMA addresses this limitation by equipping VLAs with a persistent spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond the current visual frustum. The framework consists of three components: Spatial Memory Construction, which aggregates angular-wise observations into a unified spatial-semantic representation through scanning; Dynamic Memory Refinement, which maintains global consistency over time; and Contextual Memory Retrieval, which activates instruction-relevant spatial cues during manipulation. We evaluate SOMA on five challenging real-world out-of-vision manipulation tasks, including multi-step and dual-arm scenarios where target objects are initially invisible. Experimental results show that SOMA not only improves task success rates, but also induces qualitatively different manipulation behaviors, with faster target localization, reduced viewpoint search, and near one-shot grasping under partial observability. Additional experiments on RoboCasa GR1 and SimplerEnv further validate the effectiveness of SOMA's memory design under conventional fully observable settings. Code will be released soon.
