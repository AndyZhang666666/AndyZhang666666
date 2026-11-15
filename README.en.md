<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile-dark.svg">
  <img src="assets/profile-light.svg" alt="Agent / Evaluation / Growth · a compact decision trace" width="100%">
</picture>

# Andy Zhang · 张千羽

**AI Product Manager working on Agents, evaluation and growth.**

I turn business questions into usable products, then check whether they solve the problem. These four projects show decisions about evaluation, preferences, commercial trade-offs and evidence.

[Portfolio & full demos](https://andyzhang666666.github.io/) · [Product CV, Chinese](https://andyzhang666666.github.io/assets/resume.pdf) · [中文](README.md) · [All projects](PROJECTS.en.md)

## Start here

### Eval Lab · Review a 2/5 judgement

The judge gave an unfinished story opening 2/5 for structure. Read the line it cited, then decide whether the comment holds up. I keep the judge’s original score and record the reviewer’s disagreement separately. Later, the team can revisit whether the draft or the rubric needs work. [Review and calibration changes · PR #5](https://github.com/AndyZhang666666/llm-output-eval/pull/5)

[Review a 2/5 judgement](https://andyzhang666666.github.io/llm-output-eval/?sample=e06&dimension=structure) · [Use your own draft](https://andyzhang666666.github.io/llm-output-eval/workspace/) · [Design decisions](https://andyzhang666666.github.io/cases/trust/) · [Source](https://github.com/AndyZhang666666/llm-output-eval)

[![Eval Lab · e06 · source quote and the original structure score](assets/eval-e06.jpg)](https://andyzhang666666.github.io/llm-output-eval/?sample=e06&dimension=structure)

<h3>TasteRoom</h3>
<p>Where should a preference apply?</p>
<a href="https://andyzhang666666.github.io/tasteroom/"><img src="https://raw.githubusercontent.com/AndyZhang666666/AndyZhang666666.github.io/174399eef34fcdaae22926585dcf9066d1a283bb/tasteroom/docs/evidence/task-loop-20261111/scene-desktop.png" alt="TasteRoom: Where should a preference apply?" width="100%"></a>
<p>I let people try the same poster with personal and work rules side by side. A preference is saved to a context only when the user confirms it. <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/8">Preference confirmation · PR #8</a></p>
<p><sub>Local design rules / comparison saves no preference</sub><br><a href="https://andyzhang666666.github.io/tasteroom/">Try it</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/main/tasteroom/docs/TASK-LOOP-20261111.md">Design</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom">Source</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/174399eef34fcdaae22926585dcf9066d1a283bb/tasteroom/docs/evidence/task-loop-20261111/scene-desktop.png">Full image</a></p>

<h3>Bundle Lab</h3>
<p>Can selling more earn less?</p>
<a href="https://andyzhang666666.github.io/bundle-lab/simulate/"><img src="https://raw.githubusercontent.com/AndyZhang666666/bundle-lab/062b6563a9e587c27040f6fc596184f58d0407b3/docs/assets/task-loop-20261111/workspace-1280.png" alt="Bundle Lab: Can selling more earn less?" width="100%"></a>
<p>Customers who would have bought anyway can also claim a discount. I account for that cost separately and save the break-even threshold before the trial, so later orders can be checked against the original assumptions. <a href="https://github.com/AndyZhang666666/bundle-lab/pull/4">Ledger and break-even check · PR #4</a></p>
<p><sub>Synthetic orders / personal inputs / conditional model</sub><br><a href="https://andyzhang666666.github.io/bundle-lab/simulate/">Try it</a> · <a href="https://github.com/AndyZhang666666/bundle-lab/blob/main/docs/TASK-LOOP-20261111.md">Design</a> · <a href="https://github.com/AndyZhang666666/bundle-lab">Source</a> · <a href="https://github.com/AndyZhang666666/bundle-lab/blob/062b6563a9e587c27040f6fc596184f58d0407b3/docs/assets/task-loop-20261111/workspace-1280.png">Full image</a></p>

<h3>Trustworthy RAG Lab</h3>
<p>Which source supports this number?</p>
<a href="https://andyzhang666666.github.io/rag-lab/"><img src="https://raw.githubusercontent.com/AndyZhang666666/AndyZhang666666.github.io/174399eef34fcdaae22926585dcf9066d1a283bb/rag-lab/evidence/task-loop-20261111/rag-1280-grounding.png" alt="Trustworthy RAG Lab: Which source supports this number?" width="100%"></a>
<p>A different date or reader can change which sources support the same answer. I show the two sets of sources side by side so the writer can check each number in the draft. <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/8">Compare evidence across conditions · PR #8</a></p>
<p><sub>Local retrieval and human drafts / no model call by default</sub><br><a href="https://andyzhang666666.github.io/rag-lab/">Try it</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/main/rag-lab/docs/TASK-LOOP-20261111.md">Design</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/rag-lab">Source</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/174399eef34fcdaae22926585dcf9066d1a283bb/rag-lab/evidence/task-loop-20261111/rag-1280-grounding.png">Full image</a></p>

The Eval image shows the public e06 replay on 15 November. The other three images show the actual interfaces with constructed acceptance material from 11 November. Demo links open the current products; images are pinned to their source versions. [Image provenance](docs/assets/featured-sources-20261112.json)

## Recently shipped

| Date | Released changes | Implementation record |
| --- | --- | --- |
| 2026-11-15 | [Home Notes](https://andyzhang666666.github.io/renovation/) · Compare fit and delivered cost offline. After launch I saw the new card disappear in a browser with a cached directory, fixed the cache and retested the route from the portfolio filter. | [Directory cache fix · PR #13](https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/13) · [Source](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/renovation) · [Iterations](https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/main/renovation/CHANGELOG.md) |
| 2026-11-11 | Eval: compare exact changes between saved drafts, copy the current version's task package and collect disputed evidence in a draft calibration memo. | [Eval PR #5](https://github.com/AndyZhang666666/llm-output-eval/pull/5) |
| 2026-11-11 | Bundle: adjust existing customers' discount take-up, save matrix previews as scenarios and check later counts against the plan's frozen break-even boundary. | [Bundle PR #4](https://github.com/AndyZhang666666/bundle-lab/pull/4) |
| 2026-11-11 | TasteRoom: compare scoped rules on the same copy and image. RAG: inspect draft numbers and compare evidence scope after date or role changes. | [Product release PR #8](https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/8) · [RAG asset-version patch #9](https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/9) |

## Explore further

[Agent Execution Bench](https://andyzhang666666.github.io/agent-bench/) examines lost responses, permissions and duplicate writes. [Filing Eval](https://github.com/AndyZhang666666/filing-eval) reviews factual errors and important omissions separately. [Growth Experiment Lab](https://github.com/AndyZhang666666/growth-experiment-lab) and [Pricing Model Sim](https://github.com/AndyZhang666666/pricing-model-sim) test what evidence supports a business decision.

[Suibianju](https://andyzhang666666.github.io/suibianju/), [Grounded Choice](https://andyzhang666666.github.io/grounded-choice/), [Commute Compare](https://github.com/AndyZhang666666/commute-compare) and the [poker experiments](PROJECTS.en.md#everyday-decisions-and-modelling) remain in the project index. [AI Product Teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) examines capability boundaries, failure handling and payment moments. [Creative Eval](https://github.com/AndyZhang666666/creative-eval) preserves the first iteration's calibration and historical results.

## Work in practice

At Shanhai Xingchen, I own creative Agent workflows and Skill assets: 38 Skills shipped, around 6,000 tool calls per month and roughly 30% less creation time per drama. During my Baidu internship, I helped launch an AI feature that passed 10,000 daily active users within two weeks. At Meituan Keeta, segmented subsidy experiments reduced new-customer acquisition cost by 27% and increased new-customer monthly retention by 8%. I also interned on Li Auto's smart cockpit and Revolut's subscription products.

[Responsibilities and measurement context](https://andyzhang666666.github.io/#work) · [Product CV, Chinese](https://andyzhang666666.github.io/assets/resume.pdf)

These are work outcomes. The public repositories contain independent projects, with simulated material, historical model outputs and conditional calculations labelled separately. They contain no employer code or internal business data. Public Agent / RAG demos use recorded program executions and browser retrieval respectively; live-model use requires local configuration.

Master's studies at UCL; undergraduate Electrical and Electronic Engineering at Bristol. My research includes an order-flow-based intraday trading model and a wearable posture-monitoring system with a mobile interface.

[Get in touch](https://andyzhang666666.github.io/#contact) · [中文](README.md) · [Browse all projects](PROJECTS.en.md)
