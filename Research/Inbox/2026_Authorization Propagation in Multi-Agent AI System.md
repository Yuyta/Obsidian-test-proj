---
authors:
- K. Tallam
doi: null
fetched_at: '2026-05-11 02:14:13'
status: Inbox
tags:
- paper
- automated-research
- AI-Agent
title: 'Authorization Propagation in Multi-Agent AI Systems: Identity Governance as
  Infrastructure'
url: https://www.semanticscholar.org/paper/85a0ae379fd934ad051b6b19c79f1f101361df56
year: 2026
---



## Connections
- Topic: [[AI Agent]]
- Type: [[Research Paper]]

## Abstract
The security discussion around agentic AI focuses heavily on prompt injection. This paper argues that multi-agent systems also create a distinct authorization problem: maintaining authorization invariants as non-human principals retrieve data, delegate tasks, and synthesize results across changing boundaries. We call this problem authorization propagation. It is not reducible to prompt injection and is not fully addressed by classical access-control models such as RBAC, ABAC, or ReBAC. The paper formalizes authorization propagation as a workflow-level property, identifies three sub-problems (transitive delegation, aggregation inference, and temporal validity), and derives seven structural requirements for authorization architectures in multi-agent AI systems. Recent work on invocation-bound capability tokens, task-scoped authorization envelopes, dependency-graph policy enforcement, and execution-count revocation demonstrates that the field is converging on the problem, but not yet on a complete architecture. The central claim is that identity governance must be treated as infrastructure: evaluated continuously, enforced at every interaction boundary, and designed into the system before orchestration logic is allowed to scale. Preliminary implementation evidence from a production enterprise AI platform shows that ordinary system behavior, not only adversarial action, already produces the failures this model predicts.