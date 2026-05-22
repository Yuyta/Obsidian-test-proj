---
title: "Enhancing Multimodal Large Language Models for Safety-Critical Driving Video Analysis"
authors: ['Tomaso Trinci', 'Henrique Piñeiro Monteagudo', 'Leonardo Taccari']
published: 2026-05-21
arxiv_id: 2605.22185v1
url: https://arxiv.org/abs/2605.22185v1
---

Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in general visual understanding. However, their application to safety-critical driving scenarios remains limited by an inability to accurately perceive and reason about rare high-stakes dynamic events, such as collisions or near-collisions. To address this, we introduce a pipeline that enhances MLLM perception by fusing downsampled video frames with synchronized high-frequency telematics data (IMU and GPS) and semantic insights from specialized computer vision models. Our pipeline generates high-quality pseudo-labels, including descriptive captions and question-answer pairs, specifically designed to train MLLMs to identify and describe Safety-Critical Events (SCEs) in real-world driving footage. We show the effectiveness of our approach fine-tuning the open-source QwenVL-2.5 model via DoRA adapters: our experiments demonstrate significant improvements in identifying and explaining safety-critical events, with fewer than 50M trainable parameters and limited computational budget.
