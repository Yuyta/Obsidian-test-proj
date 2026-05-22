---
title: "GSA-YOLO: A High-Efficiency Framework via Structured Sparsity and Adaptive Knowledge Distillation for Real-Time X-ray Security Inspection"
authors: ['Jiahao Kong']
published: 2026-05-20
arxiv_id: 2605.20669v1
url: https://arxiv.org/abs/2605.20669v1
---

X-ray security inspection requires accurate real-time detection of prohibited items, but existing models often struggle to balance the challenges of severe occlusion, complex clutter, and strict speed requirements. To overcome these challenges, this paper proposes GSA-YOLO, a novel lightweight framework built upon the YOLOv8n architecture, specifically engineered to enhance detection robustness and inference efficiency. GSA-YOLO strategically integrates structured sparsity and adaptive knowledge transfer through three core components: Group Lasso (GL) applied to the network neck for robust feature extraction; Sparse Structure Selection (SSS) applied to the detection head for significant model slimming; and an Adaptive Knowledge Distillation (Ada-KD) mechanism for comprehensive accuracy recovery. This integrated approach synergistically enhances feature representation while pruning redundant channels, maximizing model efficiency without sacrificing performance. Rigorous evaluations on the HiXray and PIDray datasets confirm GSA-YOLO's comprehensive capability, achieving a leading inference speed of 189.62 FPS, accompanied by a reduction in computational cost from 8.7G to 8.0G. Crucially, GSA-YOLO secures mAP50:95 results of 0.531 and 0.679 on HiXray and PIDray, demonstrating 2.4% and 1.8% improvements over the baseline, respectively. Compared to other models, GSA-YOLO exhibits enhanced accuracy while maintaining computational efficiency, making it a promising solution for practical X-ray security inspection.
