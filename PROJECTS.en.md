# Project index

[Home](README.en.md) · [中文](PROJECTS.md)

Browse by the decision each project examines. Agent Bench, RAG Lab, TasteRoom and Suibianju live inside the personal-site repository; they do not have separate repositories.

## Agents and evaluation

| Project | Product question and mechanism | Run mode |
| --- | --- | --- |
| [Agent Execution Bench](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/agent-bench) · [Demo](https://andyzhang666666.github.io/agent-bench/) | Inspect original operations and final ticket state after timeouts, with approval, permissions and idempotency. | Recorded program runs; a Python / SQLite backend runs locally. |
| [Trustworthy RAG Lab](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/rag-lab) · [Demo](https://andyzhang666666.github.io/rag-lab/) | Select applicable documents, then inspect retrieval, citations, conflicts and missing evidence. | Public BM25 retrieval and rule extraction; the local API adds server-side scope checks. |
| [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [Demo](https://andyzhang666666.github.io/llm-output-eval/) | Per-dimension scores, citation location and separate human review. | 18 saved outputs across six examples; optional model configuration. |
| [Filing Eval](https://github.com/AndyZhang666666/filing-eval) · [Demo](https://andyzhang666666.github.io/demos/filing-eval/) | Review false claims and important omissions separately against the source. | Historical replay of 28 constructed notices, with separate human review. |

## Everyday products

| Project | Product question and mechanism | Run mode |
| --- | --- | --- |
| [TasteRoom](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom) · [Demo](https://andyzhang666666.github.io/tasteroom/) | Single-variable design comparisons, scoped consent and reversible preference memory. | Original posters and local rules; no live model or image-generation call. |
| [Suibianju](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/suibianju) · [Demo](https://andyzhang666666.github.io/suibianju/) | Confirm constraints, preview voluntary changes and require agreement on the same proposal. | A single-person negotiation simulation with 3–5 fictional roles. |
| [Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [Demo](https://andyzhang666666.github.io/grounded-choice/) | Compare choices while retaining conflicting experiences and applicability. | Original simulated sources; no live search or automatic price comparison. |

## Growth and monetisation

| Project | Product question and mechanism | Run mode |
| --- | --- | --- |
| [Bundle Lab](https://github.com/AndyZhang666666/bundle-lab) · [Demo](https://andyzhang666666.github.io/bundle-lab/) | Take a basket association through a two-population ledger into a test plan. | Synthetic orders and uncalibrated behaviour assumptions. |
| [Growth Experiment Lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [Demo](https://andyzhang666666.github.io/growth-experiment-lab/) | Experiment planning, peeking risk, statistical evidence and rollout decisions. | Seeded simulations and synthetic records; no automatic rollout approval. |
| [Pricing Model Sim](https://github.com/AndyZhang666666/pricing-model-sim) · [Demo](https://andyzhang666666.github.io/pricing-model-sim/) | Compare payment mechanisms, revenue traces and payback on a conserved cohort. | Conditional revenue model; price and conversion assumptions remain uncalibrated. |

## Everyday decisions and modelling

| Project | Product question and mechanism | Run mode |
| --- | --- | --- |
| [Commute Compare](https://github.com/AndyZhang666666/commute-compare) · [Demo](https://andyzhang666666.github.io/commute-compare/) | Compare cost, duration distributions and lateness risk, using personal records for calibration. | Browser calculations; no live maps or traffic API. |
| [Bankroll Simulator](https://github.com/AndyZhang666666/poker-bankroll-sim) · [Demo](https://andyzhang666666.github.io/poker-bankroll-sim/) | Separate insufficient-stake stopping, ever reaching a target and finishing above it. | Seeded modelling exercise that retains residual balances. |
| [Poker EV Calculator](https://github.com/AndyZhang666666/poker-ev-calculator) · [Demo](https://andyzhang666666.github.io/poker-ev-calculator/) | Use effective stakes consistently and inspect decisions across assumption errors. | Single-street learning model, not a GTO solver or calibrated equity model. |

## Product writing and earlier work

- [AI Product Teardowns](https://github.com/AndyZhang666666/ai-product-teardowns): three dated analyses of Kling, Doubao and Wenku AI. Includes a reusable framework and explicitly labels implementation inferences.
- [Creative Eval](https://github.com/AndyZhang666666/creative-eval): the first Eval iteration, preserving rubric calibration and historical outputs. The current review interface is [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval). The two iterations use different samples and are not a controlled improvement comparison.

## Experience and research

The [portfolio](https://andyzhang666666.github.io/#work) separately describes professional work, enterprise delivery and research. These descriptions are not public client systems or additional source repositories. Repository-specific licences apply.
