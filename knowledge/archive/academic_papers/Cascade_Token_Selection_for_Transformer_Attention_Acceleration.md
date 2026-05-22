---
title: "Cascade Token Selection for Transformer Attention Acceleration"
authors: ['Stephen J. Thomas']
published: 2026-05-04
arxiv_id: 2605.03110v1
url: https://arxiv.org/abs/2605.03110v1
---

A method is presented for reducing the cost of representative token selection in transformer attention layers by exploiting the coherence of the representative set across depth. Activation Decorrelation Attention (ADA) selects $r \ll T$ representative tokens at each layer via a Gram threshold and computes attention on the compressed $r \times r$ problem, but the selection requires a $T \times T$ Gram matrix at every layer. The cascade mechanism introduced here inherits the representative set from layer $l$ to layer $l+1$, validates it via a $(T - r) \times r$ cross-Gram computation, and updates it with a small number of additions and removals. The cost of the selection step drops from $O(T^2 d)$ to $O(T r d)$ per layer. Validation on three model families (GPT-2 124M, GPT-J 6B, OPT 6.7B) on AMD MI300X demonstrates Gram operation savings of $22\%$ to $63\%$ with mean Jaccard overlap of $0.83$ to $0.94$ between consecutive layers. The cascade reveals that the set of informative tokens is a structural property of the input that propagates coherently through the depth of the network: the same tokens carry the non-redundant information at layer $l$ and at layer $l+1$.
