---
title: "DEFLECT: Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning for VLA Policies"
authors: ['Yixiang Zhu', 'Yonghao Chen', 'Rui Meng', 'Jingyu Guo', 'Jiaxiang Zou', 'Zijie Yang', 'Taowen Wang', 'Xinyu Chen']
published: 2026-05-19
arxiv_id: 2605.19294v1
url: https://arxiv.org/abs/2605.19294v1
---

Vision-Language-Action (VLA) policies are typically deployed with asynchronous inference: the robot executes a previously predicted action chunk while the model computes the next one. This creates a prediction-execution misalignment: the chunk is conditioned on the observation taken before inference began, but executes in a physical state that has already drifted forward by several control steps; naive asynchronous rollover collapses from 89% to under 1% on Kinetix as the inference cycle covers up to seven control steps. We introduce DEFLECT, a fully offline post-training refinement that applies as a near drop-in upgrade to existing async-VLA stacks by converting latency itself into a label-free preference signal: counterfactual fresh/stale action pairs are constructed from a frozen reference policy and scored under the deployment-time conditioning via an implicit flow-matching likelihood-ratio surrogate, with no human labels, reward models, or online rollouts. DEFLECT substantially extends the usable delay envelope of async VLA control, with +6.4 success-rate gain in the high-latency regime (5-7 control steps), +4.6 when transferred to a real-scale VLA at the longest delay, and consistent improvements on two real-robot tasks (a bimanual conveyor pick-and-place and a reactive whack-a-mole).
