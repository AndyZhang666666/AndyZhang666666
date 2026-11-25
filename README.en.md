<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/editorial/cover-narrow-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/editorial/cover-narrow-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/cover-dark.svg">
  <img src="assets/editorial/cover-light.svg" alt="张千羽 · Andy Zhang — Agent / Evaluation / Growth" width="100%">
</picture>

**Qianyu (Andy) Zhang · AI Product Manager & Builder.** I build agent workflows and evaluation tools, and test the economics of growth.

[中文](README.zh-CN.md) · [Portfolio][site] · [Résumés][cv] · [All projects](PROJECTS.en.md)

## Try a product decision

All five open without a key. Eval and Agent Bench replay records. The retrieval and business examples use constructed data.

| Project | What you can check | Try it |
| --- | --- | --- |
| [Eval Lab][repo1] | Find the sentence behind a historical 2/5. Does the rubric fit an opening scene? | [Check the quote](https://andyzhang666666.github.io/llm-output-eval/?sample=e06&dimension=structure) |
| [Agent Bench][repo2] | A write times out. Compare the receipt with the final ticket in a recorded run. | [Replay timeout](https://andyzhang666666.github.io/agent-bench/) |
| [RAG Lab][repo3] | Change the policy date. Check which passage now supports the loan period. | [Change date](https://andyzhang666666.github.io/rag-lab/) |
| [Bundle Lab][repo4] | Move a discount from 6% to 8%. See when discounts to existing buyers erase the margin. | [Try a discount](https://andyzhang666666.github.io/bundle-lab/simulate/) |
| [Growth Lab][repo5] | Conversion rises in a synthetic A/B test. Check lift and guardrails before rollout. | [Review rollout](https://andyzhang666666.github.io/growth-experiment-lab/#read) |

## How I build

- Set a failure condition before choosing evaluation samples.
- Keep the original verdict so a reviewer can challenge it with a source.
- Count the discount existing buyers receive alongside revenue from new buyers.

[7-second revision replay][replay] · [Cross-language search case][search] · [Release notes](CHANGELOG.md)

---

[Portfolio][site] · [Contact][contact]

[site]: https://andyzhang666666.github.io/
[cv]: https://andyzhang666666.github.io/#resumes
[contact]: https://andyzhang666666.github.io/#contact
[search]: https://andyzhang666666.github.io/#evidence-search
[replay]: docs/editorial/replay/eval-task-7s.gif
[repo1]: https://github.com/AndyZhang666666/llm-output-eval
[repo2]: https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/agent-bench
[repo3]: https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/rag-lab
[repo4]: https://github.com/AndyZhang666666/bundle-lab
[repo5]: https://github.com/AndyZhang666666/growth-experiment-lab
