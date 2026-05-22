---
title: "Health-Conditioned Vision-Language-Action Models for Malfunction-Aware Robot Control"
authors: ['Hüseyin Arslan', 'Özgür Erkent']
published: 2026-05-15
arxiv_id: 2605.16056v1
url: https://arxiv.org/abs/2605.16056v1
---

Research on Vision Language Action (VLA) models has been increasing rapidly in recent years. Although some of them focus on detecting, preventing, and recovering from task failures, they usually don't deal with adapting to robot's physical failures. In real-life scenarios, most robots face physical degradations in various ways such as joint degradation, actuator failure, or weak gripper. We introduce malfunction-aware (health-conditioned) VLA that takes a health vector as an input that gives information about robots' joints' operation angle and torque capability, and adapts its predictions to complete the tasks with the degraded joints. To achieve this, we inject a Health Projector module to the VLA-Adapter architecture and train it on malfunction robot data we collected on the LIBERO environment [1]. We collect 128 teleoperated episodes on Libero-Spatial tasks. Our results show that, with a very lightweight addition, the model can learn to operate successfully with different configurations of degraded joints which the default pretrained VLA-Adapter's Libero-Spatial-Pro model cannot. The code and dataset will be available soon at https://github.com/h-arslan/health-aware-vla
