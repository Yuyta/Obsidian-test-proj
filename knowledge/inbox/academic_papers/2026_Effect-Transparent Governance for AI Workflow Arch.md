---
authors:
- Alan L. McCann
doi: null
fetched_at: '2026-05-22 23:06:25'
status: Inbox
tags:
- paper
- automated-research
- AI
title: 'Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation,
  Expressive Minimality, and Decidability Boundaries'
url: https://www.semanticscholar.org/paper/9866822034e5e2b8fd9fd33f43e13b18fd861fdf
year: 2026
---



## Connections
- Topic: [[AI]]
- Type: [[Research Paper]]

## Abstract
We present a machine-checked formalization of structurally governed AI workflow architectures and prove that effect-level governance can be imposed without reducing internal computational expressivity. Using Interaction Trees in Rocq 8.19, we define a governance operator G that mediates all effectful directives, including memory access, external calls, and oracle (LLM) queries. Our development compiles with 0 admitted lemmas and consists of 36 modules, ~12,000 lines of Rocq, and 454 theorems. We establishseven properties: (P1) governed Turing completeness, (P2) governed oracle expressivity, (P3) a decidability boundary in which governance predicates are total and closed under Boolean composition while semantic program properties remain non-trivial and undecidable by governance, (P4) goal preservation for permitted executions, (P5) expressive minimality of primitive capabilities (compute, memory, reasoning, external call, observability), (P6) subsumption asymmetry showing structural governance strictly subsumes content-level filtering, and (P7) semantic transparency: on all executions where governance permits, the governed interpretation is observationally equivalent (modulo governance-only events) to the ungoverned interpretation. Together, these results show that governance and computational expressivity are orthogonal dimensions: governance constrains the effect boundary of programs while remaining semantically transparent to internal computation.