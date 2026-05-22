---
permalink: /patents/
title: "Patent-Pending AI Inventions"
author_profile: true
---

All four inventions were conceived and developed during my tenure at **Vertex Inc** (2022–2026),
addressing real-world problems in tax intelligence, audit defense, and nexus compliance.

---

## 1. Data Cake

**Domain**: Tax Data Synthesis / ML Training Data  
**Status**: Patent Pending

An NLP service that generates realistic synthetic tax data by learning the statistical properties
of real customer data using machine learning models (XGBoost, scikit-learn) plus a deterministic
rules engine that enforces tax-law constraints. Enables safe testing, model training, and product
development without exposing sensitive customer PII.

**Why it matters**: Tax companies can't easily share real transaction data. Data Cake solves the
training-data bottleneck without the compliance risk. Models trained on Data Cake performed within
2% of models trained on real data — without ever touching real customer information.

[Read the deep dive →](/engineering/ai/2025/12/11/how-data-cake-got-built.html)

---

## 2. Audit Management Red Black Tree (Timber Model)

**Domain**: Tax Audit Defense / ROI Analysis  
**Status**: Patent Pending

A self-balancing binary search tree (BST) model that determines ROI thresholds for audit defense
decisions. The tree automatically rebalances as new audit data arrives, enabling real-time
threshold recommendations for whether to contest, settle, or absorb a tax audit finding. The
"Timber" component prunes branches whose distributions have shifted out of relevance.

**Why it matters**: Audit defense decisions are traditionally gut-feel or spreadsheet-driven. This
model makes them data-driven, explainable, and fast — turning $50K judgment calls into
auditable reasoning trails.

[Read the deep dive →](/engineering/ai/2025/10/22/audit-red-black-tree-patent.html)

---

## 3. Doc Intel

**Domain**: Developer Tooling / Code Quality  
**Status**: Patent Pending

A confidence-scoring system that detects drift between source code and its documentation. As code
evolves, Doc Intel flags when documentation has fallen out of sync — giving teams a quantitative
measure of documentation health across their entire codebase.

**Why it matters**: Documentation rot is silent and expensive. Doc Intel makes it visible and
measurable, before the gap becomes a production incident or an onboarding tax.

[Read the deep dive →](/engineering/ai/2026/01/28/doc-intel-patent.html)

---

## 4. Mort AI Nexus

**Domain**: Multi-State Economic Nexus Compliance (Sales Tax)  
**Status**: Patent Pending

A predictive model that forecasts when a company crosses **economic nexus thresholds** across US
jurisdictions in the post-*Wayfair* sales-tax landscape. Each state sets its own threshold
(typically $100K in revenue or 200 transactions per year — see the [Sales Tax Institute's economic
nexus state guide](https://www.salestaxinstitute.com/resources/economic-nexus-state-guide)). Cross
the line and you owe sales tax in that state, often discovered months later via a state notice
with penalties and interest stacked on top.

Mort AI Nexus uses pattern analysis informed by Wayfair plus regional economic signals to forecast
threshold crossings 30, 60, and 90 days out — letting compliance teams register and configure
calculation in advance instead of catching up after the fact.

**Why it matters**: Per-state exposure runs $100K–$500K. Mort AI Nexus shifts discovery from
reactive ("we got a state notice") to predictive ("we'll cross in 60 days, here's what to do").

[Read the deep dive →](/engineering/ai/2026/01/14/mort-ai-nexus-patent.html)

---

*All inventions patent-pending. Details available upon request under NDA.*
