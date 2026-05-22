---
authors:
- Yifei Wei
- Linqing Zhong
- Yi Liu
- Yuxiang Lu
- Xindong He
- Maoqing Yao
- Guanghui Ren
doi: null
fetched_at: '2026-05-23 00:05:09'
status: Inbox
tags:
- paper
- automated-research
- VLA
title: 'Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine
  Dual-System'
url: https://www.semanticscholar.org/paper/b0ea98dd4a4afca9ea2dcf0d6a211db67497e194
year: 2026
---



## Connections
- Topic: [[VLA]]
- Type: [[Research Paper]]

## Abstract
Vision-Language-Action (VLA) models are a promising paradigm for generalist robotic manipulation by grounding high-level semantic instructions into executable physical actions. However, prevailing approaches typically adopt a monolithic generation paradigm, directly mapping visual-linguistic features to high-frequency motor commands in a flat, non-hierarchical fashion. This strategy overlooks the inherent hierarchy of robotic manipulation, where complex actions can be naturally modeled in a Hybrid Action Space, decomposing into discrete macro-directional reaching and continuous micro-pose alignment, severely widening the semantic-actuation gap and imposing a heavy representational burden on grounding high-level semantics to continuous actions. To address this, we introduce Libra-VLA, a novel Coarse-to-Fine Dual-System VLA architecture. We explicitly decouple the learning complexity into a coarse-to-fine hierarchy to strike a training equilibrium, while simultaneously leveraging this structural modularity to implement an asynchronous execution strategy. The Semantic Planner predicts discrete action tokens capturing macro-directional intent, while the Action Refiner conditions on coarse intent to generate high-frequency continuous actions for precise alignment. Crucially, our empirical analysis reveals that performance follows an inverted-U curve relative to action decomposition granularity, peaking exactly when the learning difficulty is balanced between the two sub-systems. With the asynchronous design, our approach offers a scalable, robust, and responsive solution for open-world manipulation.