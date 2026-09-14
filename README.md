# Andy Zhang (张千羽)

AI Product Manager at NOVA (short-drama production platform). Before that: AI product 0→1 at Baidu, user growth at Meituan (Saudi Arabia market), in-car assistant at Li Auto. UCL MSc Financial Engineering, Bristol BEng EEE.

- **AI product design** — I take a business scenario all the way to shipped AI features: agent workflow design, reusable prompt-asset management, and evaluation systems that tell you whether a new version is actually better. Comfortable working alongside algorithm teams to take AI products from 0 to 1 and scale them.
- **Data-driven, closed-loop** — SQL/Python for analysis and strategy validation; A/B testing, event-tracking attribution, and funnel decomposition to break down business problems and find growth paths that can be shipped and verified.
- **Growth & monetization** — From user-scenario insight to paid-conversion path design: identifying high-value scenarios, designing differentiated experiences, and hands-on experience with subscription rollout and promotion optimization. Overseas market experience; English as a working language.

**Try the demos → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — five interactive tools, nothing to install.

## Projects

### AI evaluation

| Project | Problem | What I built | Result |
|---|---|---|---|
| [creative-eval](https://github.com/AndyZhang666666/creative-eval) · [demo](https://andyzhang666666.github.io) | A content team gets 200 AI-generated script fragments a day; QA is still three people reading. No consistent way to say "v2 is better than v1". | An LLM judge that scores short-drama scripts on 5 fixed dimensions (hook, pacing, dialogue, persona, structure), each with written 1/3/5 anchors, and must quote evidence from the text. A 40-item golden set with human labels, and a validation suite: run-to-run stability, agreement with humans, length and order bias. | 93.1% within-±1 agreement with human raters. v1 judge was +0.38 too lenient; adding score anchors brought it to +0.23. |
| [llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval) · [demo](https://andyzhang666666.github.io/llm-output-eval/) | The judge above is a script, not a tool. PMs need to compare prompt versions and collect failure cases without touching code. | The same judge as a static web app. Paste text → per-dimension scores with verbatim evidence. Compare mode runs two versions N times each and shows mean ± range. Every ≤2 score is collected into an exportable bad-case list. Bring your own API key — calls go straight from your browser, no server. | Validation caught two bugs (truncation silently dropping samples; nulls counted as scores). Spearman ρ with humans 0.93 after the fix. |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) | AI summaries of listed-company filings occasionally turn 120M into 1.2B or invent a sentence. Subjective scoring can't catch that. | Claim-level fact checking: split the summary into claims, match each back to the filing, label supported / contradicted / unsupported, then check key-fact coverage. Tested on 20 main samples plus 8 adversarial ones with planted errors and prompt injections. | 11/11 planted errors caught, 0/4 false positives, 5/5 injections held. |

### Growth & monetization

| Project | Problem | What I built | Result |
|---|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [demo](https://andyzhang666666.github.io/growth-experiment-lab/) | Running A/B tests on coupon tiers at Meituan, the hard part wasn't the test — it was sizing it, resisting the urge to stop early, and turning "2 points of lift" into a ship/no-ship call. | A four-tab simulator: sample-size designer with an MDE curve; a peeking-penalty simulator that runs 2,000 zero-effect trials and shows what daily checking does to false positives; a result interpreter that turns the confidence interval into a conservative revenue estimate; and an experiment ledger where every decision is reproduced by the same rule the tool uses. | Peek daily and stop at first p<0.05 → false-positive rate goes from 4.95% to 22.45%. |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [demo](https://andyzhang666666.github.io/pricing-model-sim/) | Working on overseas short-drama monetization: subscription markets had 3× the repeat-purchase rate of per-episode markets. Convincing the team meant showing the same cohort under different pricing mechanics. | Drag a retention curve, set episode price / monthly fee / CAC / platform cut, and compare pay-per-episode, subscription, and hybrid on 12-month ARPU, LTV, and payback. A sensitivity sweep finds where the best mechanic flips. | Subscription only beats hybrid above roughly ¥33–38/month, and the crossover is lower the better retention is. |

### Commerce & product analysis

| Project | Problem | What I built | Result |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [demo](https://andyzhang666666.github.io/bundle-lab/) | In Meituan's Saudi market, low basket size came from a structural mismatch: many group orders, a menu built for singles. Bundle decisions were made by hand from SQL pulls. | Upload order lines → see the group-vs-single mismatch → mine co-purchase pairs with association rules (lift / support / confidence) → set discount and adoption rate to see margin impact → export a one-page "who to target, what to bundle, when not to" recommendation. Validation planted 5 known bundles in synthetic data. | Recovered 5/5 planted bundles; usable from about 2,000 orders, noise below 200. |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | Most AI product reviews are feature lists. | Three teardowns (Kling, Doubao, Wenku AI) against one fixed 6-dimension framework: capability boundary, failure handling, how effect is measured, agentic potential, cost and latency, and what I'd do next as PM. | The framework is the reusable part. |

## Contact

[github.com/AndyZhang666666](https://github.com/AndyZhang666666) · [andyzhang666666.github.io](https://andyzhang666666.github.io)

---

## 中文

AI 产品经理，目前在 NOVA（短剧内容生产平台）。此前在百度做 AI 产品 0→1，在美团做用户增长（沙特市场），在理想汽车做智能座舱。UCL 金融工程硕士，布里斯托大学电气电子工程学士。

- **AI 应用产品设计能力**：关注大模型与 AI 行业趋势，具备从业务场景需求到 Agent 工作流设计、可复用 Prompt 资产管理与效果评估体系搭建的完整方法论；能与算法团队高效协同，推动 AI 产品从 0 到 1 并规模化复制。
- **数据驱动与业务闭环**：具备产品的逻辑框架，能独立利用 SQL/Python 进行数据分析与策略验证，熟练运用 A/B Test、埋点归因与转化漏斗模型拆解业务问题，在不同业务场景找到可落地的增长路径并推动验证，形成业务直觉与闭环思维。
- **用户增长与商业化产品经验**：具备从用户场景洞察到付费转化路径设计的完整能力，能识别高价值场景并设计差异化产品体验，在订阅制推广与促销策略优化方向形成实战经验；拥有海外市场产品经历，英语可作为工作语言。

**在线 Demo → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — 五个可交互工具，不用装任何东西。

## 项目

### AI 效果评估

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [creative-eval](https://github.com/AndyZhang666666/creative-eval) · [Demo](https://andyzhang666666.github.io) | 内容团队用 AI 一天能出 200 条剧本片段，但判断质量的还是那几个人。新版 prompt 好不好，只能靠「感觉顺一点」。 | 一个短剧剧本的 LLM 评分裁判：5 个固定维度（开场钩子、节奏、对白、人设、结构），每档写死 1/3/5 分锚点，每个分数必须引用原文证据。配一套 40 条人工标注的金标集，和一套校验脚本：同一条连跑 3 次稳不稳、和人工标注一不一样、会不会看长度和顺序给分。 | 与人工标注 ±1 分一致率 93.1%。第一版裁判偏松 +0.38，加打分基准后降到 +0.23。 |
| [llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval) · [Demo](https://andyzhang666666.github.io/llm-output-eval/) | 上面那个裁判是一堆脚本，不是工具。PM 要对比 prompt 版本、收集失败样本，不该碰代码。 | 把同一个裁判做成网页工具：粘一段文本 → 逐维分数和逐字证据句。对比模式两版各连跑 N 次，给均值 ± 极差。所有 ≤2 分的维度自动收进 Bad Case 列表，可导出 CSV。自带 API key，请求从浏览器直接发给服务商，没有服务端。 | 校验时抓出两个 bug（截断导致样本静默丢失、null 被当成有效分），修完后与人工的 Spearman ρ 为 0.93。 |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) | AI 把上市公司公告压成摘要，会把 1.2 亿写成 12 亿、会凭空多一句。主观打分抓不住这类错。 | 断言级事实核查：把摘要拆成一条条断言，逐条回原文比对，标「支持 / 矛盾 / 无依据」，再查关键事实覆盖率。20 条主集 + 8 条对抗样本（故意植入错误和提示注入）。 | 植入错误检出 11/11、干净样本误报 0/4、提示注入 5/5 守住。 |

### 增长与商业化

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [Demo](https://andyzhang666666.github.io/growth-experiment-lab/) | 在美团做优惠券梯度的 A/B 验证时，难的不是跑实验，是算不清要多少样本、忍不住提前停、以及把「提升 2 个点」变成推不推的决定。 | 四个页签：实验设计器（含 MDE 曲线）；偷看惩罚模拟器，跑 2000 次零效应试验，看每天偷看对假阳性率的影响；结果解读器，用置信区间下界算最保守能拿多少收入；实验台账，每条决策都用工具里同一条规则复现。 | 每天偷看、一显著就停，假阳性率从 4.95% 涨到 22.45%。 |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [Demo](https://andyzhang666666.github.io/pricing-model-sim/) | 做海外短剧付费时，订阅制市场的复购率是单集解锁市场的三倍多。说服团队要让所有人看见同一批用户在不同付费机制下差多少。 | 拖一条留存曲线，设单集价 / 月费 / CAC / 平台抽成，比较「单次解锁 / 包月订阅 / 混合」12 个月的 ARPU、LTV、回本周期。敏感性扫描找出最优机制在哪个参数上换手。 | 月费大约在 ¥33–38 以上订阅才反超混合；留存越好，换手点越低。 |

### 电商与产品分析

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [Demo](https://andyzhang666666.github.io/bundle-lab/) | 在美团沙特市场，客单价低的原因是结构错位：很多多人点单，菜单却以单人餐为主。套餐组合靠人拉 SQL 拍脑袋定。 | 传订单明细 → 看多人单与单人单的错位 → 用关联规则（lift / support / confidence）挖「经常一起买」的组合 → 调折扣和采纳率看客单、毛利怎么变 → 导出一页「推给谁、推什么、什么情况别推」。校验用合成数据预埋 5 个已知组合。 | 召回 5/5；2000 单起可用，200 单以下是噪声。 |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | 多数 AI 产品评测是功能清单。 | 用同一套六维框架拆解可灵、豆包、文库 AI：能力边界、答错时怎么办、效果怎么衡量、智能体潜力、成本时延、如果我是 PM 下一步做什么。 | 框架是可复用的部分。 |

## 联系

[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
