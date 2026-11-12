<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/editorial/cover-narrow-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/editorial/cover-narrow-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/cover-dark.svg">
  <img src="assets/editorial/cover-light.svg" alt="Andy Zhang · 张千羽 — Agent / Evaluation / Growth" width="100%">
</picture>

**Andy Zhang · AI Product Manager working on Agents, evaluation and growth.**

I turn business questions into usable products, then check whether they solve the problem.

[Portfolio & full demos](https://andyzhang666666.github.io/) · [Product CV, Chinese](https://andyzhang666666.github.io/assets/resume.pdf) · [中文](README.md) · [All projects](PROJECTS.en.md)

## Eval Lab

**After a rewrite, does the judgement still hold?**

Compare the original and revised drafts, inspect the exact additions and deletions, then take the current version's evaluation task package with you.

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/editorial/eval-narrow-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/editorial/eval-narrow-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/eval-dark.svg">
  <img src="assets/editorial/eval-light.svg" alt="Eval Lab: source evidence, human judgement and revision comparison" width="100%">
</picture>

**A quotation can exist while the judgement is wrong.** Model scores and human observations are saved separately; each revised draft keeps its own review context.

The image uses constructed text for manual review and version comparison, with no model call. Historical outputs have a separate replay.

[Try it](https://andyzhang666666.github.io/llm-output-eval/workspace/) · [Design & implementation](docs/editorial/projects/eval.md)

[Watch the 7-second task replay](docs/editorial/replay/eval-task-7s.gif)

## Three more projects

### TasteRoom

Does a personal preference also belong at work? Compare the same copy and image under personal and work rules, then decide where a preference should apply.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/taste-dark.svg">
  <img src="assets/editorial/taste-light.svg" alt="TasteRoom: the same copy and image under personal and work consent" width="100%">
</picture>

**Viewing and trying a design do not save a lasting preference.** Saving requires an explicit choice and scope.

Local design-rule demo. Viewing the comparison does not write to preference memory.

[Try it](https://andyzhang666666.github.io/tasteroom/) · [Design & implementation](docs/editorial/projects/taste.md)

### Bundle Lab

Can selling another bundle earn less? Build a baseline from product or CSV inputs, put new contribution, discounts to existing customers and the margin change in one ledger, then freeze a plan for later observations.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/bundle-dark.svg">
  <img src="assets/editorial/bundle-light.svg" alt="Bundle Lab: new contribution, existing-customer discounts and margin change" width="100%">
</picture>

**Extra purchases may not cover the discounts.** Later observations are checked against the frozen plan, rather than a threshold that moves with the current inputs.

Conditional calculations using synthetic orders or your own inputs. Margin changes exclude fulfilment and operating costs; they are not verified business returns.

[Try it](https://andyzhang666666.github.io/bundle-lab/simulate/) · [Design & implementation](docs/editorial/projects/bundle.md)

### Trustworthy RAG Lab

Which source supports this number? Import material, select citations, edit a draft, then inspect its numbers and evidence scope when the date or role changes.

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/editorial/rag-narrow-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/editorial/rag-narrow-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/rag-dark.svg">
  <img src="assets/editorial/rag-light.svg" alt="Trustworthy RAG: draft numbers, source evidence and scope warnings" width="100%">
</picture>

**A matching number is a clue; a change in source scope calls for another check.** The hints do not establish semantic correctness.

Local browser retrieval, rule-based checks and human-edited drafts. No model calls by default.

[Try it](https://andyzhang666666.github.io/rag-lab/) · [Design & implementation](docs/editorial/projects/rag.md)

## Recently shipped

- **2026-11-11 · Eval** — Save revisions, inspect exact changes and copy the current version's evaluation task package; collect disputed evidence in a draft calibration memo. [Release record](https://github.com/AndyZhang666666/llm-output-eval/pull/5)
- **2026-11-11 · Bundle** — Adjust existing-customer discount take-up, save matrix previews as scenarios and check observed counts against a frozen break-even plan. [Release record](https://github.com/AndyZhang666666/bundle-lab/pull/4)
- **2026-11-11 · TasteRoom / RAG** — Compare personal and work consent using the same content; check draft numbers and compare evidence scope before and after date or role changes. [Release record](https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/8)

## Experience and other work

<details>
<summary>Work experience, business outcomes and research</summary>

At Shanhai Xingchen, I own creative Agent workflows and Skill assets: 38 Skills shipped, around 6,000 tool calls per month and roughly 30% less creation time per drama. During my Baidu internship, I helped launch an AI feature that passed 10,000 daily active users within two weeks. At Meituan Keeta, segmented subsidy experiments reduced new-customer acquisition cost by 27% and increased new-customer monthly retention by 8%. I also interned on Li Auto's smart cockpit and Revolut's subscription products.

[Responsibilities and measurement context](https://andyzhang666666.github.io/#work) · [Product CV, Chinese](https://andyzhang666666.github.io/assets/resume.pdf)

These are work outcomes. The public repositories contain independent projects, with simulated material, historical model outputs and conditional calculations labelled separately. They contain no employer code or internal business data. Public Agent / RAG demos use recorded program executions and browser retrieval respectively; live-model use requires local configuration.

Master's studies at UCL; undergraduate Electrical and Electronic Engineering at Bristol. My research includes an order-flow-based intraday trading model and a wearable posture-monitoring system with a mobile interface.

</details>

The full index retains Agent execution evaluation, other evaluation tools, Suibianju, Grounded Choice, growth and pricing, commuting, poker and product analysis.

[Agents and evaluation](PROJECTS.en.md#agents-and-evaluation) · [Everyday products](PROJECTS.en.md#everyday-products) · [Growth and monetisation](PROJECTS.en.md#growth-and-monetisation) · [Everyday decisions and modelling](PROJECTS.en.md#everyday-decisions-and-modelling) · [Product writing and earlier work](PROJECTS.en.md#product-writing-and-earlier-work)

[Get in touch](https://andyzhang666666.github.io/#contact) · [中文](README.md) · [Browse all projects](PROJECTS.en.md)

[Image sources and versions](docs/editorial/SOURCES.md)
