---
title: "Making the Discrete Continuous: Synthetic RAW Augmentations for Fine-Grained Evaluation of Person Detection Performance in Low Light"
authors: ['Valeria Pais', 'Malena Mendilaharzu', 'Daniele Faccio', 'Luis Oala', 'Christoph Clausen', 'Bruno Sanguinetti']
published: 2026-05-21
arxiv_id: 2605.22455v1
url: https://arxiv.org/abs/2605.22455v1
---

Real-world deployment of AI vision models is both fueled and limited by the data available for training and testing. Real datasets are sparse and uneven: long-tailed or unbalanced distributions hinder generalization, and the low number of samples in low density regions makes it hard to run evaluations. Synthetic data can fill these gaps, providing us with a way to sample the input space more continuously and improve data coverage for benchmarks. Focusing on the autonomous driving safety-critical case of pedestrian detection in the dark, we show how synthetic low-light samples can be used to better characterize the performance of a state-of-the-art object detection model as a function of the scene illumination. We use a synthetic RAW image augmentation technique to generate low-light samples that match the noise model of the camera sensor. Performance metrics on real and synthetic low-light data are similar, indicating that the AI model finds it hard to distinguish between them.
