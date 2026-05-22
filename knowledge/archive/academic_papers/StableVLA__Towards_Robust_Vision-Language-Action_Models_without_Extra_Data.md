---
title: "StableVLA: Towards Robust Vision-Language-Action Models without Extra Data"
authors: ['Yiyang Fu', 'Chubin Zhang', 'Shukai Gong', 'Yufan Deng', 'Kaiwei Sun', 'Qiyang Min', 'Qibin Hou', 'Yansong Tang', 'Jianan Wang', 'Daquan Zhou']
published: 2026-05-18
arxiv_id: 2605.18287v1
url: https://arxiv.org/abs/2605.18287v1
---

It is infeasible to encompass all possible disturbances within the training dataset. This raises a critical question regarding the robustness of Vision-Language-Action (VLA) models when encountering unseen real-world visual disturbances, particularly under imperfect visual conditions. In this work, we conduct a systematic study based on recent state-of-the-art VLA models and reveal a significant performance drop when visual disturbances absent from the training data are introduced. To mitigate this issue, we propose a lightweight adapter module grounded in information theory, termed the Information Bottleneck Adapter (IB-Adapter), which selectively filters potential noise from visual inputs. Without requiring any extra data or augmentation strategies, IB-Adapter consistently improves over the baseline by an average of 30%, while adding fewer than 10M parameters, demonstrating notable efficiency and effectiveness. Furthermore, even with a 14x smaller backbone (0.5B parameters) and no pre-training on the Open X-Embodiment dataset, our model StableVLA achieves robustness competitive with 7B-scale state-of-the-art VLAs. With negligible parameter overhead (<10M), our approach maintains accuracy on long-horizon tasks and surpasses OpenPi under both synthetic and physical visual corruptions.
