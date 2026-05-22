---
authors:
- Mingtao Gao
- Julia Maria Perathoner
- Anton Ludwig Bonin
- S. Eulig
- Gianni Klesse
doi: null
fetched_at: '2026-05-22 23:06:34'
status: Inbox
tags:
- paper
- automated-research
- MLOps
title: Robust and Reliable AI for Predictive Quality in Semiconductor Materials Manufacturing
  with MLOps and Uncertainty Quantification
url: https://www.semanticscholar.org/paper/77373f0994f99e021292f3c4fc5ee742c9b351c8
year: 2026
---



## Connections
- Topic: [[MLOps]]
- Type: [[Research Paper]]

## Abstract
Semiconductor materials manufacturing presents unique challenges for machine learning deployment due to evolving process conditions, equipment degradation, and raw material variability that can cause model performance deterioration over time. This study benchmarks machine learning operations (MLOps) retraining strategies using five years of real manufacturing data to identify optimal retraining approaches for quality prediction. We evaluate various retraining frequencies and hyperparameter optimization strategies using control limit normalized residuals as key performance metric. Results demonstrate that a fixed retraining cadence every five production batches without hyperparameter retuning achieves superior performance across all drift conditions while significantly reducing computational overhead compared to strategies incorporating hyperparameter optimization. This approach effectively maintains model accuracy during both abrupt process changes and gradual equipment degradation patterns. To address the critical need for uncertainty quantification in manufacturing decision-making, we implement conformal prediction to generate prediction confidence intervals with strong statistical guarantees. This enables proactive quality control by identifying when prediction intervals fall within acceptable control limits, transforming traditional reactive quality management into a predictive framework. The findings provide practical guidelines for implementing robust MLOps strategies in manufacturing environments where computational efficiency and reliable uncertainty quantification are paramount for operational success.