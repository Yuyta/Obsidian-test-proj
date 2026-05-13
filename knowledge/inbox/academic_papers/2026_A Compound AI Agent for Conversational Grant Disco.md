---
authors:
- Zhi–Bin Tang
- M. Kejriwal
doi: null
fetched_at: '2026-05-11 02:14:13'
status: Inbox
tags:
- paper
- automated-research
- AI-Agent
title: A Compound AI Agent for Conversational Grant Discovery
url: https://www.semanticscholar.org/paper/6310d2722cc25f1b225940539ee01d71b0695926
year: 2026
---



## Connections
- Topic: [[AI Agent]]
- Type: [[Research Paper]]

## Abstract
Research funding discovery remains fundamentally fragmented: researchers navigate disparate agency portals (e.g., in the United States, NSF, NIH, DARPA, Grants.gov, and many others) with heterogeneous interfaces, search capabilities, and data schemas. We present a compound AI system that unifies this landscape through two tightly coupled components: (1) an aggregation layer that autonomously collects, normalizes, and indexes almost 12,000 federal and nonprofit opportunities from fragmented sources via LLM-equipped browser agents, maintaining a biweekly-updated unified database; and (2) an agentic ReAct-based query processing layer that interprets research context (including from PDF documents) and employs hybrid search combining a structured index with selective web search to retrieve relevant opportunities - while avoiding LLM hallucination. The conversational interface supports iterative refinement through multi-turn interactions, allowing researchers to progressively apply constraints without reformulating their core research description. Results stream in real time with full transparency of intermediate reasoning, enabling appropriate calibration of user trust. Currently used by almost 3,000+ users, our approach demonstrates the feasibility of compound AI in reducing grant discovery time from 30--45 minutes (manual, fragmented portal searches) to under 10 minutes (unified, conversational search).