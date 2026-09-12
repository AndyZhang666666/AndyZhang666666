# Andy Zhang (张千羽)

**AI Product Manager** — I build agent workflows, prompt-asset platforms, and the evaluation systems that keep them honest. Currently at NOVA, a short-drama production platform.

Previously: AI product 0→1 at Baidu, user growth at Meituan (Saudi Arabia), and in-car assistant at Li Auto.

**Start here → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — score a script yourself, then compare against the human labels and two judge versions. No code to read.

## What I work on

- **Agent workflow design** — multi-stage task orchestration with human checkpoints at every stage
- **Prompt asset governance** — turning ad-hoc prompts into versioned, staged-rollout assets with tracked outcomes
- **Evaluation systems** — golden sets, LLM-as-judge, bad-case attribution, judge reliability testing
- **Monetization & growth** — subscription mechanics, event-tracking attribution, A/B testing

The through-line: **shipping an AI feature is the easy half. Proving this version is better than the last one is the hard half.** Every repo below is about that second half.

## Projects

| Project | What it is |
|---|---|
| [llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval) | Eval harness for long-form generated text — 5 dimension scores with verbatim evidence, plus a report validating the judge itself |
| [creative-eval](https://github.com/AndyZhang666666/creative-eval) | Scoring judge for short-drama scripts — 5 weighted dimensions, 93.1% agreement with human labels |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) | Claim-level fact-checking for AI-generated filing summaries — 11/11 error detection, 0 false positives |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | Teardowns of Chinese AI products against a fixed 6-dimension framework |
| note-intent-classifier | WIP — classifying note intent on Xiaohongshu to predict lead quality |
| pricing-model-sim | WIP — subscription vs. one-time pricing revenue simulator |

The last two have no link on purpose — no repo yet, and a dead link is worse than no link.

## Background & Contact

- **NOVA** — AI Product Manager (agent workflows, prompt platform, overseas subscription)
- **Baidu · Meituan · Li Auto** — AI product 0→1, user growth, in-car assistant
- **UCL** — MSc Financial Engineering · **University of Bristol** — BEng Electrical & Electronic Engineering
- Working languages: Chinese, English
- [github.com/AndyZhang666666](https://github.com/AndyZhang666666) · [andyzhang666666.github.io](https://andyzhang666666.github.io)

---

## 中文

AI 产品经理。做 Agent 工作流、Prompt 资产平台，以及让它们可控的效果评估体系。目前在 NOVA（短剧内容生产平台）。此前在百度做 AI 产品的 0→1，在美团做用户增长，在理想汽车做智能座舱。

**我关注的问题是一个具体的问题：AI 产品做出来了，怎么证明它到底好不好。**

大模型产品最难的不是让它跑起来，是回答「这版比上一版好在哪、好多少」。评审会上的意见永远是「感觉不对」——没法量化，也没法比较。下面几个仓库都在这条线上：不是包个模型做应用，是给已有的 AI 产品建一套能复现、能反驳、能拿去开评审会的评估体系。

### 项目

**[llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval)** — 长文本生成质量的评测工具。五个维度用 LLM-as-judge 打分并强制给出逐字证据句，附一份裁判自身的可靠性校验报告（连跑一致性、与人工标注的比对、位置偏差）。报告里如实写了找到的两个 bug：响应被 max_tokens 截断导致样本静默丢失，以及空值污染统计聚合。

**[creative-eval](https://github.com/AndyZhang666666/creative-eval)** — 短剧剧本的评分裁判。与人工标注 ±1 分一致率 93.1%，同输入连跑 3 次加权标准差 0.074。第一版裁判系统性偏松（比人工高 +0.38），加打分基准后降到 +0.21，前后数据都在仓库里。

**[filing-eval](https://github.com/AndyZhang666666/filing-eval)** — 公告摘要的断言级事实核查。把摘要拆成断言逐条回原文核对，错误检出 11/11、误报 0/4、提示注入 5/5 守住。

**[ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns)** — 用固定六维框架拆解可灵、豆包、文库 AI。框架本身比结论更重要：能力边界在哪、答错时怎么办、效果怎么衡量、如果我是 PM 下一步做什么。

### 两类评估的差别

creative-eval 评**主观质量**——没有标准答案，只能靠 rubric 锚点加人工标注一致率证明裁判没跑偏。filing-eval 评**客观事实**——有唯一正确答案，可以直接算检出率和误报率，但要小心指标之间互相掩盖。同一套 LLM-as-judge 的手法，两种问题的度量方式完全不同。这个差别是我做完才真正想清楚的。

### 踩过的坑

- **三个指标 AND 成一个，等于自己骗自己。** 摘要把数字写错了，那条关键事实必然显示「未覆盖」——检出和覆盖在错误样本上互相打架，AND 起来永远不及格。
- **「检出率 100%」可能是分母算错了。** 干净样本被标签规则误算成错误样本，检出率虚高到 15/15，真实值是 11/11。
- **一片绿色比报错更可怕。** 4 条测试样本写了期望值却因判定逻辑走标签而一项都没执行，静默显示通过。加空测试检测器才抓出来。
- **裁判和我不一致时，先怀疑自己的标注。** 但不改标注去迁就裁判——那等于把测试集调成永远通过。

联系：[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
