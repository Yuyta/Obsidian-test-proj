---
authors:
- Zhuoren Li
- B. Leng
- Lu Xiong
- A. Eichberger
- Chao Huang
- Jia Hu
doi: 10.1109/TITS.2026.3670584
fetched_at: '2026-05-22 23:09:20'
status: Inbox
tags:
- paper
- automated-research
- autonomous-driving
title: 'Safety-Enhanced Deep Reinforcement Learning for Autonomous Driving: Dare to
  Make Mistakes to Learn Better and Faster'
url: https://www.semanticscholar.org/paper/55f105f615e4c563843a6c968ff942400aca64fc
year: 2026
---



## Connections
- Topic: [[autonomous driving]]
- Type: [[Research Paper]]

## Abstract
Deep Reinforcement Learning (DRL) is becoming a prominent method for autonomous driving due to its strong capability to generate complex driving policy. However, DRL motion planning still has limitations in safety performance including learning quality, convergence speed and the safety guarantee. To this end, this work proposes a safety-enhanced deep reinforcement learning method with dynamic safety guidance (DSG-DRL) for lane-change motion planning. It bears the following key features: 1) Able to learn a safer DRL driving policy by additionally including potentially unsafe behaviors; 2) Able to accelerate learning a safe policy by making dangerous driving experiences impressive; 3) Able to further enhance the driving safety by avoiding unexpected reckless action. The proposed DSG-DRL motion planner dares to make mistakes to learn the safe driving policy better and faster. By evaluating anticipated risk, it learns not only from the maneuvers right at the moments of collisions, but also from the dangerous maneuvers leading towards collisions. Besides, risk driving experiences are enhanced with additional memory batches and sampling prioritization. Moreover, reckless actions can be prevented by dynamic constraints both in training and testing, which further improves the safety performance. Simulation validation shows that the proposed method can learn a safer driving policy with faster convergence speed, achieving the high safety performance while keeping the driving efficiency.