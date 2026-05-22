---
title: "H-Flow: Self-supervised Human Scene Flow via Physics-inspired Joint Multi-modal Learning"
authors: ['Zhanbo Huang', 'Xiaoming Liu', 'Yu Kong']
published: 2026-05-21
arxiv_id: 2605.22629v1
url: https://arxiv.org/abs/2605.22629v1
---

Parametric human models capture global pose but cannot represent the non-rigid surface dynamics of clothing and soft tissue. Generic scene flow estimates dense motion but breaks down on articulated bodies, where pixel-level supervision is also intractable to acquire. We introduce H-Flow, a dense human scene flow that captures both skeletal kinematics and surface deformation. A unified multi-head transformer estimates flow from monocular video, jointly predicting pose and depth as companion outputs. The challenge lies in the lack of supervision. In place of unattainable labels, we anchor the network in the physics of human motion, encoding geometric, structural, and biomechanical priors as cross-modal training objectives. We further introduce DynAct4D, a high-fidelity synthetic benchmark providing dense flow annotations across diverse subjects, garments, and motions. On standard benchmarks, H-Flow outperforms scene-flow and parametric baselines, and generalizes zero-shot to in-the-wild video. Code, models, and the DynAct4D benchmark will be released upon publication
