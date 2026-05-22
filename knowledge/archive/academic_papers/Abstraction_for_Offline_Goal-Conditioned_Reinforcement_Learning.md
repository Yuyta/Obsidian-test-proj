---
title: "Abstraction for Offline Goal-Conditioned Reinforcement Learning"
authors: ['Clarisse Wibault', 'Alexander Goldie', 'Antonio Villares', 'Maike Osborne', 'Jakob Foerster']
published: 2026-05-21
arxiv_id: 2605.22711v1
url: https://arxiv.org/abs/2605.22711v1
---

Markov Decision Processes (MDPs) often exhibit significant redundancy due to symmetries and shared structure across state-goal pairs in real-world Goal-Conditioned Reinforcement Learning (GCRL). While hierarchical policies have been motivated for horizon reduction via temporal abstraction in offline GCRL, we demonstrate that hierarchy also enables absolute abstraction. By introducing relativised options as well as distinct representations for different levels of the hierarchy, we demonstrate how an agent can reuse experience across similar contexts of the state-space. Based on this framework, we introduce two simple algorithms for learning relativised options and abstracting from the absolute frame of reference. Our experiments show that such inductive biases significantly improve performance in offline GCRL.
