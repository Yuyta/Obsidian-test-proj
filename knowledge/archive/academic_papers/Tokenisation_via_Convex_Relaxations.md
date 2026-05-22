---
title: "Tokenisation via Convex Relaxations"
authors: ['Jan Tempus', 'Philip Whittington', 'Craig W. Schmidt', 'Dennis Komm', 'Tiago Pimentel']
published: 2026-05-21
arxiv_id: 2605.22821v1
url: https://arxiv.org/abs/2605.22821v1
---

Tokenisation is an integral part of the current NLP pipeline. Current tokenisation algorithms such as BPE and Unigram are greedy algorithms -- they make locally optimal decisions without considering the resulting vocabulary as a whole. We instead formulate tokeniser construction as a linear program and solve it using convex optimisation tools, yielding a new algorithm we call ConvexTok. We find ConvexTok consistently improves intrinsic tokenisation metrics and the bits-per-byte (BpB) achieved by language models; it also improves downstream task performance, but less consistently. Furthermore, ConvexTok allows the user to certify how far their tokeniser is from optimal, with respect to a certain objective, via a lower bound, and we empirically find it to be within 1\% of optimal at common vocabulary sizes.
