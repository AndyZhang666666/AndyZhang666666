<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/editorial/cover-narrow-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/editorial/cover-narrow-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/editorial/cover-dark.svg">
  <img src="assets/editorial/cover-light.svg" alt="Andy Zhang" width="100%">
</picture>

**张千羽 · AI 产品经理。** 我做 Agent 工作流、模型评测和增长实验。下面五个工具各留了一道可以亲手验证的问题。

[English](README.md) · [个人网站][site] · [三份简历][cv] · [完整项目索引](PROJECTS.md)

## 试一次产品判断

五个体验都可以直接打开。评测与执行台回放留档记录。检索与商业算例使用构造材料。

| 项目 | 你要判断什么 | 体验 |
| --- | --- | --- |
| [Eval Lab][repo1] | 核对历史 2/5 评语引用的半句话。用完整短篇的标准评开场，合适吗？ | [Demo](https://andyzhang666666.github.io/llm-output-eval/?sample=e06&dimension=structure) |
| [Agent Bench][repo2] | 提交后回执丢失。对照两条程序回放，查工单到底改了几次。 | [Demo](https://andyzhang666666.github.io/agent-bench/) |
| [RAG Lab][repo3] | 借用期限随政策日期变化。换一个日期，核对回答引用了哪版条款。 | [Demo](https://andyzhang666666.github.io/rag-lab/) |
| [Bundle Lab][repo4] | 折扣从 6% 调到 8%。算算给老顾客的让利何时吃掉新增毛利。 | [Demo](https://andyzhang666666.github.io/bundle-lab/simulate/) |
| [Growth Lab][repo5] | 模拟实验转化上升。核对最低业务提升和护栏，决定是否放量。 | [Demo](https://andyzhang666666.github.io/growth-experiment-lab/#read) |

## 我怎么做产品

- 先写下什么结果算失败，再为评测选样本。
- 保留模型原判，让审阅者能引用原文提出异议。
- 把新增收益和既有让利列在同一张账上。

[7 秒人工改稿回放][replay] · [跨语言搜索案例][search] · [更新记录](CHANGELOG.md)

---

[个人网站][site] · [联系我][contact]

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
