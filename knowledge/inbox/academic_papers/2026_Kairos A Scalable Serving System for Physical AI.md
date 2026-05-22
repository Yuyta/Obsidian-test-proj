---
authors:
- Yinwei Dai
- Ganesh Ananthanarayanan
- Landon P. Cox
- Xenofon Foukas
- B. Radunovic
- Ravi Netravali
doi: null
fetched_at: '2026-05-23 00:02:51'
status: Inbox
tags:
- paper
- automated-research
- Physical-AI
title: 'Kairos: A Scalable Serving System for Physical AI'
url: https://www.semanticscholar.org/paper/51644547363a419afe7c832e90c9cd4c5176484d
year: 2026
---



## Connections
- Topic: [[Physical AI]]
- Type: [[Research Paper]]

## Abstract
Physical AI is experiencing rapid growth with frontier foundation models increasing its capabilities across general environments. Physical AI tasks are characterized by inference properties that are markedly different from digital AI. They consist of multiple rounds of inference and action execution, generating a chunk of actions in each inference round, and asynchronously interleaving inference and execution. This makes existing digital AI serving systems unsuited for physical AI; a shortcoming that is critical for enabling their wide adoption, considering their size and the scale of the robot fleets they have to serve. To fill this gap, we design Kairos, the first multi-robot serving system that makes the generate-execute loop a first-class citizen, with active involvement in the execution phase. Across a wide range of physical AI models and robots, Kairos reduces the average end-to-end task latency by 31.8--66.5% over state-of-the-art digital AI serving practices, with gains scaling with the robot fleet size.