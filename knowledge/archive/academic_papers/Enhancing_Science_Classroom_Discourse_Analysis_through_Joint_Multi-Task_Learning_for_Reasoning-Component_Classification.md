---
title: "Enhancing Science Classroom Discourse Analysis through Joint Multi-Task Learning for Reasoning-Component Classification"
authors: ['Jiho Noh', 'Mukhesh Raghava Katragadda', 'Raymond Carl', 'Soon Lee']
published: 2026-04-22
arxiv_id: 2604.21137v2
url: https://arxiv.org/abs/2604.21137v2
---

Analyzing the reasoning patterns of students in science classrooms is critical for understanding knowledge construction mechanism and improving instructional practice to maximize cognitive engagement, yet manual coding of classroom discourse at scale remains prohibitively labor-intensive. We present an automated discourse analysis system (ADAS) that jointly classifies teacher and student utterances along two complementary dimensions: Utterance Type and Reasoning Component derived from our prior CDAT framework. To address severe label imbalance among minority classes, we (1) stratify-resplit the annotated corpus, (2) apply LLM-based synthetic data augmentation targeting minority classes, and (3) train a dual-probe head RoBERTa-base classifier. A zero-shot GPT-5.4 baseline achieves macro-F1 of 0.467 on UT and 0.476 on RC, establishing meaningful upper bounds for prompt-only approaches motivating fine-tuning. Beyond classification, we conduct discourse pattern analyses including UTxRC co-occurrence profiling, Cognitive Complexity Index (CCI) computation per session, lag-sequential analysis, and IRF chain analysis, revealing that teacher Feedback-with-Question (Fq) moves are the most consistent antecedents of student inferential reasoning (SR-I). Our results demonstrate that LLM-based augmentation meaningfully improves UT minority-class recognition, and that the structural simplicity of the RC task makes it tractable even for lexical baselines.
