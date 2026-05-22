---
title: "SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference"
authors: ['Anay Chauhan', 'Gurucharan Marthi Krishna Kumar', 'Arion Das', 'Amit Dhanda', 'Vinija Jain', 'Aman Chadha', 'Amitava Das']
published: 2026-05-13
arxiv_id: 2605.18856v1
url: https://arxiv.org/abs/2605.18856v1
---

Long-context inference is increasingly constrained by the KV cache: resident memory grows with context length, and decoding becomes limited by repeated High Bandwidth Memory (HBM) streaming rather than arithmetic. Existing methods such as eviction, windowing, quantization, and offloading reduce footprint, but often leave the critical-path bottleneck only partially addressed, especially when compressed states must still be reconstructed into dense vectors during decoding.
  We present Spherical KV, a long-context inference method that treats KV allocation as a rate-distortion problem grounded in attention geometry for efficient decoding. The method is built on two ideas: (i) represent directional information cheaply in the decode hot loop, and (ii) allocate retention and precision according to estimated future utility. Its first component, Angle-Domain Attention (ADA), stores keys in a spherical parameterization consisting of a scalar radius and compact angle codes, and computes attention logits directly from these codes without reconstructing dense keys. This preserves a paged, block-local, fusion-friendly decode path and directly targets HBM traffic in realistic serving settings. Its second component, Rate-Distortion Retention (RDR), jointly chooses keep/drop decisions and precision tiers per token and head under a fixed budget, producing tier-homogeneous pages with lightweight metadata and coalesced reads. Together, ADA and RDR provide a deployment-oriented mechanism for reducing KV residency while preserving decode efficiency.
