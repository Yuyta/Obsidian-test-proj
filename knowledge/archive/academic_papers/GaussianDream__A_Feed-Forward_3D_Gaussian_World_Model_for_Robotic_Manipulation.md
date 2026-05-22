---
title: "GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation"
authors: ['Zijian Zhang', 'Yuqing Jiang', 'Qian Cheng', 'Si Liu', 'Ding Zhao', 'Ping Luo', 'Weitao Zhou', 'Haibao Yu']
published: 2026-05-20
arxiv_id: 2605.20752v1
url: https://arxiv.org/abs/2605.20752v1
---

Vision-language-action (VLA) policies have advanced language-conditioned robotic manipulation by transferring semantic priors from pretrained vision-language models to action generation. Yet, standard action-imitation training often provides limited explicit supervision for 3D geometry, dense visual structure, and short-horizon environment evolution, which are critical for physically precise manipulation. We introduce \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in that turns robot trajectories into structured spatial-temporal supervision. The key idea is to couple current Gaussian reconstruction with horizon-conditioned future Gaussian prediction during training, forcing a compact spatio-temporal prefix to be decodable into renderable 3D Gaussian states. This enables dense RGB rendering, depth, and pseudo 3D scene-flow supervision without requiring test-time Gaussian decoding. At inference, GaussianDream discards all auxiliary decoding heads and retains only the learned prefix to condition action generation, avoiding rendering, video rollout, or additional planning during closed-loop control. Experiments on LIBERO, RoboCasa Human-50, and real-robot tasks demonstrate strong and highly competitive performance, achieving \textbf{98.4\%} average success on LIBERO, \textbf{52.6\%} on RoboCasa Human-50, and \textbf{50.0\%} in real-world evaluation.
