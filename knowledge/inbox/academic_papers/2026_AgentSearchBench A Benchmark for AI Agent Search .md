---
authors:
- Bin Wu
- Arastun Mammadli
- Xiaoyu Zhang
- Emine Yilmaz
doi: null
fetched_at: '2026-05-22 23:09:24'
status: Inbox
tags:
- paper
- automated-research
- AI-Agent
title: 'AgentSearchBench: A Benchmark for AI Agent Search in the Wild'
url: https://www.semanticscholar.org/paper/5e0ad2bd6906e48fd8465e55d7dd5dd5d765a61e
year: 2026
---



## Connections
- Topic: [[AI Agent]]
- Type: [[Research Paper]]

## Abstract
The rapid growth of AI agent ecosystems is transforming how complex tasks are delegated and executed, creating a new challenge of identifying suitable agents for a given task. Unlike traditional tools, agent capabilities are often compositional and execution-dependent, making them difficult to assess from textual descriptions alone. However, existing research and benchmarks typically assume well-specified functionalities, controlled candidate pools, or only executable task queries, leaving realistic agent search scenarios insufficiently studied. We introduce AgentSearchBench, a large-scale benchmark for agent search in the wild, built from nearly 10,000 real-world agents across multiple providers. The benchmark formalizes agent search as retrieval and reranking problems under both executable task queries and high-level task descriptions, and evaluates relevance using execution-grounded performance signals. Experiments reveal a consistent gap between semantic similarity and actual agent performance, exposing the limitations of description-based retrieval and reranking methods. We further show that lightweight behavioral signals, including execution-aware probing, can substantially improve ranking quality, highlighting the importance of incorporating execution signals into agent discovery. Our code is available at https://github.com/Bingo-W/AgentSearchBench.