# Andy Zhang (张千羽)

**AI Product Manager** — I build agent workflows, prompt-asset platforms, and the evaluation systems that keep them honest. Currently at NOVA, a short-drama production platform.

Previously: AI product 0→1 at Baidu, user growth at Meituan (Saudi Arabia), and in-car assistant at Li Auto.

**Start here → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — five interactive demos, no code to read. Score a script yourself, then see whether the judge agrees with the humans; watch what "peeking" at an A/B test does to your false-positive rate; find the price at which subscription beats pay-per-episode.

## What I work on

- **Agent workflow design** — multi-stage task orchestration with human checkpoints at every stage
- **Prompt asset governance** — turning ad-hoc prompts into versioned, staged-rollout assets with tracked outcomes
- **Evaluation systems** — golden sets, LLM-as-judge, bad-case attribution, judge reliability testing
- **Growth & monetization** — A/B test design and stopping rules, pricing-mechanism simulation, bundle mining from order data

The through-line: **shipping is the easy half. Proving this version is better than the last one — or that this change was worth making — is the hard half.** Evaluation is the main line; but growth and pricing decisions also have to be the kind that numbers can refute. Every repo below is about that second half, and every number in every README can be traced to a file in `results/` or `validation/`.

## Projects

**Evaluation — is the AI output any good?**

| Project | One line | A number you can check |
|---|---|---|
| [creative-eval](https://github.com/AndyZhang666666/creative-eval) · [demo](https://andyzhang666666.github.io) | Scoring judge for short-drama scripts, 5-dimension rubric, plus the report on whether the judge itself is trustworthy | 93.1% within-±1 agreement with human labels (36 labeled items × 5 dimensions); v1 judge was +0.38 too lenient, v2 is +0.23 |
| [llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval) · [demo](https://andyzhang666666.github.io/llm-output-eval/) | Second version of the judge as a daily tool: two prompt versions run N times side by side, ≤2-score dimensions collected as bad cases, every score backed by a verbatim quote | Fixing a `max_tokens` truncation bug moved Spearman ρ from a polluted 0.79 to a real 0.93 |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) | Claim-level fact-checking for AI-generated filing summaries | 11/11 planted errors caught, 0/4 false positives, 5/5 prompt injections held |

**Growth & monetization — was the change worth it?**

| Project | One line | A number you can check |
|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [demo](https://andyzhang666666.github.io/growth-experiment-lab/) | A/B test decision simulator: sample size, when to stop, whether the lift is worth shipping | Peeking daily and stopping at the first significant result pushes false positives from 4.95% to 22.45% (2,000 simulated 14-day tests, zero true effect) |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [demo](https://andyzhang666666.github.io/pricing-model-sim/) | Pay-per-episode vs. subscription vs. hybrid: 12-month ARPU / LTV / payback from a retention curve | Subscription only beats hybrid once the monthly price passes ¥33–38; the better the retention, the lower the crossover |

**Commerce & teardowns — what does the data actually say?**

| Project | One line | A number you can check |
|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [demo](https://andyzhang666666.github.io/bundle-lab/) | Mines order data for bundles worth making, and bounds what a discount can earn or lose | Recovers 5/5 planted bundles; usable from 2,000 orders, pure noise below 200 |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | Teardowns of Chinese AI products against a fixed 6-dimension framework | — (no numbers to verify; the framework is the deliverable) |

Not on the list on purpose: a Xiaohongshu note-intent classifier that is still an idea, not a repo. A dead link is worse than no link.

## Background & Contact

- **NOVA** — AI Product Manager (agent workflows, prompt platform, overseas subscription)
- **Baidu · Meituan · Li Auto** — AI product 0→1, user growth, in-car assistant
- **UCL** — MSc Financial Engineering · **University of Bristol** — BEng Electrical & Electronic Engineering
- Working languages: Chinese, English
- [github.com/AndyZhang666666](https://github.com/AndyZhang666666) · [andyzhang666666.github.io](https://andyzhang666666.github.io)

---

## 中文

AI 产品经理。做 Agent 工作流、Prompt 资产平台，以及让它们可控的效果评估体系。目前在 NOVA（短剧内容生产平台）。此前在百度做 AI 产品的 0→1，在美团做用户增长，在理想汽车做智能座舱。

**我关注的问题是一个具体的问题：东西做出来了，怎么证明它到底好不好。**

大模型产品最难的不是让它跑起来，是回答「这版比上一版好在哪、好多少」。评审会上的意见永远是「感觉不对」——没法量化，也没法比较。评估是主线；但增长和商业化的判断——样本量够不够、该不该提前停、买断还是订阅、这个套餐打几折——同样得是能被数字反驳的东西，不然也是「感觉」。下面的仓库都在这条线上，每一个 README 里的每个数字都能在 `results/` 或 `validation/` 里找到出处。

### 项目

**评估：AI 做出来的东西好不好**

**[creative-eval](https://github.com/AndyZhang666666/creative-eval)** · [Demo](https://andyzhang666666.github.io) — 短剧剧本的评分裁判，第一版。5 维 rubric、40 条金标集，重点是回答「裁判自己可信吗」：与人工标注 ±1 分一致率 93.1%，同输入连跑 3 次加权标准差 0.074。第一版裁判系统性偏松（比人工高 +0.38），加打分基准后降到 +0.23，前后数据都在仓库里。

**[llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval)** · [Demo](https://andyzhang666666.github.io/llm-output-eval/) — 同一个裁判的第二版，做成能日常用的工具：两版 prompt 各连跑 N 次做对比、≤2 分的维度自动收进 Bad Case 导出、每个分数附从原文逐字抽出的证据句。校验报告里如实写了找到的两个 bug：`max_tokens` 截断导致样本静默丢失，以及空值污染统计聚合——修完后 ρ 从被污染的 0.79 回到真实的 0.93。纯静态站，自带 key 即可跑，key 只在你的浏览器里。

**[filing-eval](https://github.com/AndyZhang666666/filing-eval)** — 公告摘要的断言级事实核查。把摘要拆成断言逐条回原文核对，错误检出 11/11、误报 0/4、提示注入 5/5 守住。

**增长与商业化：这个改动值不值**

**[growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab)** · [Demo](https://andyzhang666666.github.io/growth-experiment-lab/) — A/B 实验的决策模拟器：样本量够不够、什么时候能停、提升值不值得全量。最有用的一个数：两组真实转化率完全一样时，每天偷看一显著就停，假阳性率从 4.95% 飙到 **22.45%**（2000 次 14 天零效应模拟，449 次提前停止全是假阳性）。台账里 10 条实验的决策全部能被同一个 `interpret()` 函数独立复现。

**[pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim)** · [Demo](https://andyzhang666666.github.io/pricing-model-sim/) — 给一条留存曲线，算「单次解锁 / 包月订阅 / 混合」12 个月的 ARPU、LTV、回本周期。最有说服力的一个结果：月费在 **¥33–38** 以上订阅才反超混合，而且留存越好换手点越低（社交类 ¥33.25，短剧类 ¥37.75）。

**电商与拆解：数据到底说了什么**

**[bundle-lab](https://github.com/AndyZhang666666/bundle-lab)** · [Demo](https://andyzhang666666.github.io/bundle-lab/) — 从订单里找值得做成套餐的组合，并把折扣的收益边界算清楚。合成数据预埋 5 个组合，**召回 5/5**；**2000 单起可用，200 单以下是噪声排序**。

**[ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns)** — 用固定六维框架拆解可灵、豆包、文库 AI。框架本身比结论更重要：能力边界在哪、答错时怎么办、效果怎么衡量、如果我是 PM 下一步做什么。

### 两类评估的差别

creative-eval 评**主观质量**——没有标准答案，只能靠 rubric 锚点加人工标注一致率证明裁判没跑偏。filing-eval 评**客观事实**——有唯一正确答案，可以直接算检出率和误报率，但要小心指标之间互相掩盖。同一套 LLM-as-judge 的手法，两种问题的度量方式完全不同。这个差别是我做完才真正想清楚的。

增长和商业化那三个仓库又是第三种：没有「裁判」，只有模型。校验的办法是**预埋答案**——合成数据里故意放进已知的组合、已知的效应量、手算的 LTV，看工具能不能把它们原样挖出来。挖不出来就是模型错了，不是数据错了。

### 踩过的坑

- **三个指标 AND 成一个，等于自己骗自己。** 摘要把数字写错了，那条关键事实必然显示「未覆盖」——检出和覆盖在错误样本上互相打架，AND 起来永远不及格。（filing-eval）
- **「检出率 100%」可能是分母算错了。** 干净样本被标签规则误算成错误样本，检出率虚高到 15/15，真实值是 11/11。（filing-eval）
- **一片绿色比报错更可怕。** 4 条测试样本写了期望值却因判定逻辑走标签而一项都没执行，静默显示通过。加空测试检测器才抓出来。（filing-eval）
- **裁判和我不一致时，先怀疑自己的标注。** 但不改标注去迁就裁判——那等于把测试集调成永远通过。（creative-eval）
- **先修量具，再拿它评判改动。** `max_tokens` 截断把一条样本三次全打成 null，下游又把 null 当有效分聚合，MAE 被拉高、报告看起来仍然合理。ρ 从 0.79 回到 0.93 靠的不是改 prompt，是修 bug。（llm-output-eval）
- **别在已有校验实现的代码库里第二次手写近似公式。** Bonferroni 边界我用了个近似式，还随手标注「和精确值差 0.01%」——实际高估 22%，假阳性率被压到荒谬的 0.40%。改成从已校验的 `stats.js` 导入后是 2.30%。（growth-experiment-lab）
- **文案和数字打架，和伪造数据是同一件事。** 合成台账的复盘是手写的，写着「显著 p=0.02」，数据抽样出来 p=0.15。修法不是改文案凑数，是让数字生成文案，再加断言：决策必须能被同一个函数复现。（growth-experiment-lab）
- **不报错的错最贵。** 混合机制的门槛判断把「人数 × 集数」拿去和「人均集数」比，四个数量级的量纲错——没有异常、没有 NaN，只是混合和纯解锁的 LTV 小数点后十位都一样。校验只查「是不是正数」就全漏。（pricing-model-sim）
- **跑出「全都不行」，先怀疑口径，不要先怀疑参数。** 收益估算 50 个组合 49 个亏，原因是拿整单毛利减套餐毛利——等于要求套餐一个人扛起整单利润。基线改成「这几件的原花费」后只剩 1 个不可行，而且那个结论运营能直接用。（bundle-lab）

联系：[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
