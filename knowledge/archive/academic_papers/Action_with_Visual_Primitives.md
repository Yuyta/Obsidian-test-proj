---
title: "Action with Visual Primitives"
authors: ['Weilong Guo', 'Yuchen Wang', 'Renping Zhou', 'Yunfeng Zhang', 'Rui Fang', 'Yue Meng', 'Wenda Xu', 'Yuan He', 'Gao Huang']
published: 2026-05-21
arxiv_id: 2605.22183v1
url: https://arxiv.org/abs/2605.22183v1
---

Vision-Language-Action (VLA) models have emerged as a promising paradigm for generalist robotic manipulation. A common design in current architectures maps language instructions and visual observations to actions in a single forward pass. While conceptually simple, this formulation entangles instruction comprehension, spatial scene understanding, and motor control within a single learning objective. As a result, the action expert must implicitly relearn cognitive and perceptual capabilities already present in the pretrained VLM, which can limit both learning efficiency and generalization. We introduce AVP (Action with Visual Primitives), an end-to-end architecture that implements this visual-primitive-centric interface: the VLM infers the next-stage target and emits visual-primitive tokens that condition a flow-matching action expert, with supervision derived from end-effector kinematics. Real-robot experiments on general pick-and-place tasks show that AVP improves the success rate by 27.61% over pi_0.5 and outperforms other recent methods, with consistent gains in data efficiency, spatial-compositional generalization, and object-level transfer.
