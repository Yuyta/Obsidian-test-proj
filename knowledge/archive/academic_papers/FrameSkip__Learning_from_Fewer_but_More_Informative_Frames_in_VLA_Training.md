---
title: "FrameSkip: Learning from Fewer but More Informative Frames in VLA Training"
authors: ['Bin Yu', 'Shijie Lian', 'Xiaopeng Lin', 'Zhaolong Shen', 'Yuliang Wei', 'Changti Wu', 'Hang Yuan', 'Haishan Liu', 'Bailing Wang', 'Cong Huang', 'Kai Chen']
published: 2026-05-13
arxiv_id: 2605.13757v1
url: https://arxiv.org/abs/2605.13757v1
---

Vision-Language-Action (VLA) policies are commonly trained from dense robot demonstration trajectories, often collected through teleoperation, by sampling every recorded frame as if it provided equally useful supervision. We argue that this convention creates a temporal supervision imbalance: long low-change segments dominate the training stream, while manipulation-critical transitions such as alignment, contact, grasping, and release appear only sparsely. We introduce FrameSkip, a data-layer frame selection framework that scores trajectory frames using action variation, visual-action coherence, task-progress priors, and gripper-transition preservation, then remaps training samples toward high-importance frames under a target retention ratio. Because FrameSkip operates only in the dataloader, it leaves the VLA architecture, action head, training objective, and inference procedure unchanged. Across RoboCasa-GR1, SimplerEnv, and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training and simpler frame selection variants, achieving a macro-average success rate of 76.15% across the three benchmarks compared with 66.50% for full-frame training while using a compressed trajectory view that retains 20% of unique frames in the main setting.
