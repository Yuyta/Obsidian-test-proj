---
title: "Reducing Political Manipulation with Consistency Training"
authors: ['Long Phan', 'Devin Kim', 'Alexander Pan', 'Alice Blair', 'Adam Khoja', 'Dan Hendrycks']
published: 2026-05-21
arxiv_id: 2605.22771v1
url: https://arxiv.org/abs/2605.22771v1
---

Large language models (LLMs) exhibit systematic political bias across a variety of sensitive contexts. We find that LLMs handle counterpart topics from opposing political sides asymmetrically. We refer to this phenomenon as covert political bias and identify 7 categories of techniques through which it operates. We propose two metrics for covert bias: Sentiment Consistency measures symmetry in rhetoric and framing across paired political prompts; Helpfulness Consistency measures symmetric depth and engagement. To reduce both types of covert bias, we introduce Political Consistency Training (PCT), an RL training method with two complementary paradigms: Sentiment Consistency Training and Helpfulness Consistency Training. We show that PCT preserves overall helpfulness, substantially reduces covert political bias, and generalizes to held-out benchmarks. We release our work at https://political-manipulation.ai
