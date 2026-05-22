---
title: "Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation"
authors: ['Nicanor Mayumu', 'Xiaoheng Deng', 'Patrick Mukala']
published: 2026-05-17
arxiv_id: 2605.17268v1
url: https://arxiv.org/abs/2605.17268v1
---

We present the first systematic study of faithfulness in Vision-Language-Action (VLA) driving models, analyzing 300 Alpamayo-R1-10B inferences across 100 diverse PhysicalAI-AV scenarios. Our main finding is that output natural-language rationales with trajectories may be significantly unfaithful: (i) overall reasoning fidelity is only 42.5%, with Chain-of-Causation matching scene reality less than half the time; (ii) 94 missed pedestrians in one-third of pedestrian-relevant scenes; (iii) 97.7% trajectory fragility under mild visual perturbations; and (iv) only 48.3% mean reasoning-action consistency, with 53.3% of inferences exhibiting low consistency, including 37.9% of stop-claimed cases where the model continues instead. We formalize faithfulness information-theoretically, define entity and action fidelity with verification criteria, and outline a four-component safety architecture aligned with these results.
