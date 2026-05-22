---
authors:
- Alan L. McCann
doi: null
fetched_at: '2026-05-22 23:03:07'
status: Inbox
tags:
- paper
- automated-research
- AI
title: 'The Two Boundaries: Why Behavioral AI Governance Fails Structurally'
url: https://www.semanticscholar.org/paper/b32c7671f795085a9430ed9a4c066d72b1636a6e
year: 2026
---



## Connections
- Topic: [[AI]]
- Type: [[Research Paper]]

## Abstract
Every system that performs effects has two boundaries: what it can do (expressiveness) and what governance covers (governance). In nearly all deployed AI systems, these boundaries are defined independently, creating three regions: governed capabilities (the only useful region), ungoverned capabilities (risk), and governance policies that address non-existent capabilities (theater). Two of the three regions are failure modes. We focus on the governance of effects: actions that AI systems perform in the world (API calls, database writes, tool invocations). This is distinct from the governance of model outputs (content quality, bias, fairness), which operates at a different level and requires different mechanisms. We present a formal framework for analyzing this structural gap. Rice's theorem (1953) proves the gap is undecidable in the general case for any Turing-complete architecture that attempts to govern effects behaviorally: no algorithm can decide non-trivial semantic properties of arbitrary programs, including the property"this program's effects comply with the governance policy."We define coterminous governance: a system property where the expressivenessboundary equals the governance boundary. We show that coterminous governance requires an architectural decision (separatingcomputation from effect) rather than a governance layer added after the fact. We show that structural governance under this separation subsumes separate governance infrastructure: governance checks become part of the execution pipeline rather than a second system running alongside it. We propose coterminous governance as the testable criterion for any AI governance system: either the two boundaries are provably identical, or risk and theater are structurally inevitable. Proofs are mechanized in Coq (454 theorems, 36 modules, 0 admitted).