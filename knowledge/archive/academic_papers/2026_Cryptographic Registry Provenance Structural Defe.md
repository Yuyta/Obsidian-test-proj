---
authors:
- Alan L. McCann
doi: null
fetched_at: '2026-05-11 00:22:12'
status: Inbox
tags:
- paper
- automated-research
- AI
title: 'Cryptographic Registry Provenance: Structural Defense Against Dependency Confusion
  in AI Package Ecosystems'
url: https://www.semanticscholar.org/paper/e47447aa086c1feba4a92ceb8bd3acacace816af
year: 2026
---



## Connections
- Topic: [[AI]]
- Type: [[Research Paper]]

## Abstract
Dependency confusion attacks exploit a structural gap in software distribution: once a package is installed, there is no cryptographic proof of which registry distributed it. Every existing defense is configuration-based and fails silently when misconfigured. We present a cryptographic distribution provenance system comprising three components: (1) cryptographic registry identity, where every registry holds an Ed25519 keypair and signs every artifact it distributes; (2) a dual-signature model, where the publisher signs at packaging time and the registry countersigns at publication time; and (3) authoritative namespace binding, where consumers pin registry fingerprints and the resolver cryptographically rejects artifacts from unauthorized registries. These create three defense layers requiring simultaneous compromise for a successful attack. A comparison across eight ecosystems (npm, Cargo, Hex.pm, PyPI, Go modules, Docker/OCI, NuGet, Maven) shows no existing ecosystem combines mandatory publisher signing, cryptographic registry identity, mandatory registry countersigning, and consumer-side cryptographic enforcement. The system extends to AI-generation provenance as a signed attribute and governance-enforced dependency resolution. A case study integrates distribution provenance with a three-layer runtime governance architecture, creating a four-phase lifecycle chain with no cryptographic gaps.