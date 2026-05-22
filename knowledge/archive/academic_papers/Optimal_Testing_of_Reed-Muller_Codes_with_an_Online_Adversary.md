---
title: "Optimal Testing of Reed-Muller Codes with an Online Adversary"
authors: ['Esty Kelman', 'Uri Meir', 'Kai Zhe Zheng']
published: 2026-05-21
arxiv_id: 2605.22813v1
url: https://arxiv.org/abs/2605.22813v1
---

Motivated by applications to property testing in the online-erasure model of Kalemaj, Raskhodnikova, and Varma (ITCS 2022 and Theory of Computing 2023), we define and analyze {\em semi-sample-based testers} for Reed-Muller codes. The task in Reed-Muller testing is to determine whether an input function $f: \F^n \to \F$ belongs to the Reed-Muller code or is far from it, using as few point queries to $f$ as possible. Reed-Muller testing is a well-studied task with its roots in both the Property Testing and Probabilistically Checkable Proofs literature. The online-erasure model introduces a twist: after each query made, an adversary may erase up to $t$ points of the input function, potentially thwarting any test in which the queries follow a predictable pattern.
  Semi-sample-based testers are a hybrid between sample-based testers -- which can only make uniformly random queries to the input function -- and standard testers, which can choose their queries freely. They are designed with the online-erasure model in mind and operate by first choosing some subset $S$ of the domain and then making their queries uniformly at random inside of $S$. We describe semi-sample-based testers for the Reed-Muller code and give an optimal analysis of their soundness.
  Consequently, we show that semi-sample-based testers are indeed effective in the presence of online erasures, and thereby achieve optimal query complexity for testing the Reed-Muller code in the online-erasure model. This result improves upon prior work of Minzer and Zheng (SODA 2024). As an added bonus, we show that semi-sample-based testers also exist for the lifted affine-invariant codes of Guo, Kopparty, and Sudan (ITCS 2013), thereby providing the first known testers for these codes in the online-erasure model.
