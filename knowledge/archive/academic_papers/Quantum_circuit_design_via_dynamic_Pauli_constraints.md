---
title: "Quantum circuit design via dynamic Pauli constraints"
authors: ['James R. Wootton', 'Merlin Incerti-Medici', 'Daniel Bultrini', 'Pierre Fromholz']
published: 2026-05-21
arxiv_id: 2605.22744v1
url: https://arxiv.org/abs/2605.22744v1
---

We introduce a novel software-oriented model of quantum computation motivated by the practical constraints of near-term quantum hardware. In this model, gates are specified by constraints expressed in terms of Pauli observables, with each disjoint layer of gates accompanied by a pairwise or $k$-local quantum state tomography of the device. We prove that the model is equivalent to the coupling-graph-restricted circuit model and hence universal for BQP, with a polynomial overhead: simulating a depth-$D$ circuit on $N$ qubits requires at most $O(D^2 N \log N)$ complexity. The model formalizes an idiom shared by existing work that ranges from quantum imaginary time evolution for the study of quantum systems to the use of quantum computers for procedural generation in games. It therefore provides a natural interface for designing quantum software entirely in terms of physically observable quantities, relevant for the NISQ era and into fault-tolerance.
