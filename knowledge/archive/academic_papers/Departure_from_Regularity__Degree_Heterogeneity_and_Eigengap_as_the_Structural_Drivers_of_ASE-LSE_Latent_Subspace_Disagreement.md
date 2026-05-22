---
title: "Departure from Regularity: Degree Heterogeneity and Eigengap as the Structural Drivers of ASE-LSE Latent Subspace Disagreement"
authors: ['Minh Triet Pham', 'Ian Gallagher']
published: 2026-05-21
arxiv_id: 2605.22346v1
url: https://arxiv.org/abs/2605.22346v1
---

Two of the most widely used methods for analysing graph data, Adjacency Spectral Embedding and Laplacian Spectral Embedding, often produce different results when applied to the same network. Yet the structural reasons behind this disagreement remain incompletely understood. This paper provides a structural account. We show that regularity is a sufficient condition for perfect agreement: when every node has the same number of connections, the two methods produce identical latent subspaces. Any departure from this regularity introduces disagreement, and we prove an explicit bound whose two terms suggest the structural ingredients controlling it: degree heterogeneity, which pushes the methods apart, and community structure strength, which pulls them back together. We validate both drivers empirically across thousands of simulated networks, confirming that heterogeneity drives disagreement up, community strength suppresses it, and their ratio provides a strong predictor of when the two embeddings can be treated as interchangeable and when they cannot.
