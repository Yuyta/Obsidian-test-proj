---
authors:
- Stavros Bouras
- Ioannis Korontanis
- Antonios Makris
- Konstantinos Tserpes
doi: null
fetched_at: '2026-05-22 23:06:34'
status: Inbox
tags:
- paper
- automated-research
- MLOps
title: Enabling Adversarial Robustness in AI Models through Kubeflow MLOps
url: https://www.semanticscholar.org/paper/a684411f5298ea51e5147163e2fdb431267d7b72
year: 2026
---



## Connections
- Topic: [[MLOps]]
- Type: [[Research Paper]]

## Abstract
AI models are increasingly deployed in cloud-native environments to support scalable and automated services. However, while platforms such as Kubernetes provide strong infrastructure orchestration, security mechanisms specifically designed to protect deployed AI models remain limited. This paper presents security measures for AI models deployed in Kubernetes clusters. The proposed architecture integrates Kubeflow-based MLOps to automatically detect adversarial attacks during the inference phase and trigger defense mechanisms that preserve the model's accuracy and reliability. Specifically, a Fast Gradient Sign Method (FGSM) attack is applied at inference time, and a Projected Gradient Descent (PGD)-based adversarial training defense is automatically deployed when a degradation in accuracy is detected. The experimental results indicate that the deployed defense robustifies the model, significantly recovering accuracy relative to the degradation caused by the attack.