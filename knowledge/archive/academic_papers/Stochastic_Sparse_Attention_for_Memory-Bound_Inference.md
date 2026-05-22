---
title: "Stochastic Sparse Attention for Memory-Bound Inference"
authors: ['Kyle Lee', 'Corentin Delacour', 'Kevin Callahan-Coray', 'Kyle Jiang', 'Can Yaras', 'Samet Oymak', 'Tathagata Srimani', 'Kerem Y. Camsari']
published: 2026-05-03
arxiv_id: 2605.01910v1
url: https://arxiv.org/abs/2605.01910v1
---

Autoregressive decoding becomes bandwidth-limited at long contexts, as generating each token requires reading all $n_k$ key and value vectors from KV cache. We present Stochastic Additive No-mulT Attention (SANTA), a method that sparsifies value-cache access by sampling $S \ll n_k$ indices from the post-softmax distribution and aggregates only those value rows. This yields an unbiased estimator of the post-softmax value aggregation while replacing value-stage multiply-accumulates with gather-and-add. We introduce stratified sampling to design variance-reduced, GPU-friendly variants, demonstrating $1.5\times$ decode-step attention kernel speedup over FlashInfer and FlashDecoding on an NVIDIA RTX 6000 Ada while matching baseline accuracy at 32k-token contexts. Finally, we propose Bernoulli $qK^\mathsf{T}$ sampling as a complementary technique to sparsify the score stage, reducing key-feature access through stochastic ternary queries. Both methods are orthogonal to upstream techniques such as ternary quantization, low-rank projections, and KV-cache compression. Together, they point toward sparse, multiplier-free, and energy-efficient inference. We open-source our kernels at: https://github.com/OPUSLab/SANTA.git
