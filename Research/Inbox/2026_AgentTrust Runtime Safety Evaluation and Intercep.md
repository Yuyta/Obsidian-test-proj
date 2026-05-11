---
authors:
- Chen Yang
doi: null
fetched_at: '2026-05-11 02:14:13'
status: Inbox
tags:
- paper
- automated-research
- AI-Agent
title: 'AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use'
url: https://www.semanticscholar.org/paper/93d8f04eeb2d3fb53de9d2594fa075b2fa3cfb69
year: 2026
---



## Connections
- Topic: [[AI Agent]]
- Type: [[Research Paper]]

## Abstract
Modern AI agents execute real-world side effects through tool calls such as file operations, shell commands, HTTP requests, and database queries. A single unsafe action, including accidental deletion, credential exposure, or data exfiltration, can cause irreversible harm. Existing defenses are incomplete: post-hoc benchmarks measure behavior after execution, static guardrails miss obfuscation and multi-step context, and infrastructure sandboxes constrain where code runs without understanding what an action means. We present AgentTrust, a runtime safety layer that intercepts agent tool calls before execution and returns a structured verdict: allow, warn, block, or review. AgentTrust combines a shell deobfuscation normalizer, SafeFix suggestions for safer alternatives, RiskChain detection for multi-step attack chains, and a cache-aware LLM-as-Judge for ambiguous inputs. We release a 300-scenario benchmark across six risk categories and an additional 630 independently constructed real-world adversarial scenarios. On the internal benchmark, the production-only ruleset achieves 95.0% verdict accuracy and 73.7% risk-level accuracy at low-millisecond end-to-end latency. On the 630-scenario benchmark, evaluated under a patched ruleset and not claimed as zero-shot, AgentTrust achieves 96.7% verdict accuracy, including about 93% on shell-obfuscated payloads. AgentTrust is released under the AGPL-3.0 license and provides a Model Context Protocol server for MCP-compatible agents.