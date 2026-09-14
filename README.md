# Andy Zhang (张千羽)

AI Product Manager. I work on agent workflows, prompt-asset platforms and evaluation systems, and on user growth and monetization.

- **AI product design** — From a business scenario to a shipped AI feature: agent workflow design, reusable prompt-asset management, and evaluation systems that tell you whether the new version is actually better. Work closely with algorithm teams to take AI products from 0 to 1 and scale them.
- **Data-driven, closed-loop** — SQL/Python for analysis and strategy validation; A/B testing, event-tracking attribution and funnel decomposition to break down business problems, find growth paths that can be shipped, and verify them.
- **Growth & monetization** — From user-scenario insight to paid-conversion path design: spotting high-value scenarios, designing differentiated experiences, hands-on with subscription rollout and promotion optimization. Overseas market experience; English as a working language.

The projects below are what these three look like in practice. **Try the demos → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — eight interactive tools, nothing to install.

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

### Poker & Everyday Decisions

| Project | Problem | What I built | Result |
|---|---|---|---|
| [poker-bankroll-sim](https://github.com/AndyZhang666666/poker-bankroll-sim) · [demo](https://andyzhang666666.github.io/poker-bankroll-sim/) | "Bring 20 buy-ins" is a long-standing rule of thumb — roughly right, but no one tells you whether those 20 buy-ins mean a 5% or a 40% bust probability, or what happens when your win rate slips from 52% to 50%. | Enter starting bankroll, buy-in size, win rate and variance; run 100/500/1,000 Monte Carlo simulations and output the bankroll curve (10 sample paths + median + p10/p90 bands), bust probability, target-hit probability and max drawdown. Three preset scenarios (conservative / balanced / aggressive), plus an analytic solution (first-passage of continuous Brownian motion) to cross-check the simulation. | At 10,000 sims (fixed seed), the conservative preset busts 2.64% of the time (target hit 75.60%), balanced 29.61%, aggressive 42.69%. Doubling buy-in size from 2.5% to 5% of bankroll pushes the bust rate from 2.6% to 29.6% — a step change, not a linear one. |
| [poker-ev-calculator](https://github.com/AndyZhang666666/poker-ev-calculator) · [demo](https://andyzhang666666.github.io/poker-ev-calculator/) | Most EV calculators are either too complex (you must enter an exact opponent range) or too simple (pot odds only, ignoring who the opponent is and what they did). This tool sits in between. | Enter three observable inputs — hand strength, opponent type, opponent action — to estimate equity, then lay fold / call / raise expected value side by side. A bar chart compares the three decisions, the best is highlighted with a reason, and a sensitivity tab sweeps hand strength 0→100 to find the crossover where calling becomes correct. 8 classic spots one-click fill, 169 starting-hand strength lookup. Key fix: raise EV uses post-call equity, not raw equity — once an opponent calls your raise their range is stronger, and skipping that discount overvalues raising. | 8/8 cases match expectation. Preflop AA vs a raise: raise EV +42.50 is best. Turn straight draw: call +100.00 beats raise +84.00. 72o: fold is best. The crossover strength (e.g. 50 for case 1) says how much you can be wrong and still be safe. |
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [demo](https://andyzhang666666.github.io/commute-compare/) | Map apps recommend a route with one number — "about 42 minutes". But the real decision needs a distribution: the subway is ~40 min and barely varies; a cab's median is 30 min but 70 in traffic. The lower-average option can be the more often-late one. | Enter 2–6 commute options (each with fast / typical / slow times and one-way cost); a PERT distribution plus 2,000-month Monte Carlo gives monthly total time, monthly total cost, late probability, and the departure time that keeps lateness at a level you accept. Two charts: arrival-time density (area right of the red line = late probability) and departure-time vs late-probability (drag the threshold to see each option's latest safe departure). Presets for Hangzhou / Beijing / Shanghai / Shenzhen; not city-locked. PERT over normal because commute times are right-skewed. | Hangzhou (Jinshahu → Xihu), N=5,000 months, work 09:30, 5% threshold: subway P50 36.54h/mo, ¥264, leave 08:32, late 3.53%; cab P50 29.07h/mo, ¥1,980, leave 08:37, late 4.99%. The cab is 7.5h faster per month yet needs to leave earlier for the same on-time rate, and costs ¥1,716 more. |

## Contact

[github.com/AndyZhang666666](https://github.com/AndyZhang666666) · [andyzhang666666.github.io](https://andyzhang666666.github.io)

---

## 中文

AI 产品经理。做 Agent 工作流、Prompt 资产平台和效果评估体系，也做用户增长与商业化。

- **AI 应用产品设计能力**：关注大模型与 AI 行业趋势，具备从业务场景需求到 Agent 工作流设计、可复用 Prompt 资产管理与效果评估体系搭建的完整方法论；能与算法团队高效协同，推动 AI 产品从 0 到 1 并规模化复制。
- **数据驱动与业务闭环**：具备产品的逻辑框架，能独立利用 SQL/Python 进行数据分析与策略验证，熟练运用 A/B Test、埋点归因与转化漏斗模型拆解业务问题，在不同业务场景找到可落地的增长路径并推动验证，形成业务直觉与闭环思维。
- **用户增长与商业化产品经验**：具备从用户场景洞察到付费转化路径设计的完整能力，能识别高价值场景并设计差异化产品体验，在订阅制推广与促销策略优化方向形成实战经验；拥有海外市场产品经历，英语可作为工作语言。

下面的项目是这三条能力的具体样子。**在线 Demo → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — 八个可交互工具，不用装任何东西。

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

### 德州扑克与日常决策

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [poker-bankroll-sim](https://github.com/AndyZhang666666/poker-bankroll-sim) · [Demo](https://andyzhang666666.github.io/poker-bankroll-sim/) | 「带 20 个买入」是圈子里流传已久的经验规则，大致对，但没人告诉你这 20 个买入对应的破产概率到底是 5% 还是 40%，也没人告诉你胜率从 52% 掉到 50% 时会发生什么。 | 输入起始资金、每次买入金额、胜率、方差，蒙特卡洛跑 100/500/1,000 场，输出资金曲线（10 条模拟路径 + 中位数 + p10/p90 分位带）、破产概率、达标概率、最大回撤。三个预设场景（保守 / 平衡 / 激进），附一份解析解（连续布朗运动的首次穿越）用来交叉验证模拟结果。 | 10,000 次模拟（固定种子）：保守型破产率 2.64%（达标率 75.60%），平衡型 29.61%，激进型 42.69%。买入从本金 2.5% 提到 5%，破产率从 2.6% 跳到 29.6%——是数量级差别，不是线性放大。 |
| [poker-ev-calculator](https://github.com/AndyZhang666666/poker-ev-calculator) · [Demo](https://andyzhang666666.github.io/poker-ev-calculator/) | 市面上的 EV 计算器要么太复杂（要输入精确对手范围），要么太简单（只算底池赔率，不管对手是谁、做了什么动作）。这个工具取中间。 | 输入三个可观测项——手牌强度、对手类型、对手动作——估胜率，把弃牌 / 跟注 / 加注三个决策的期望收益摆在一起比。柱状图对比三个决策，最优项高亮并给理由，敏感性 tab 把手牌强度 0→100 扫一遍，找「跟注变对」的交叉点。8 个经典场景一键填充，169 种起手牌强度查表。关键修正：加注 EV 用「被跟注后的胜率」而非原始胜率——对手愿意跟你的加注说明他范围变强了，少这层折价加注会被系统性高估。 | 8/8 案例与预期一致。翻牌前 AA vs 加注：加注 EV +42.50 最优。转牌顺子听牌：跟注 +100.00 优于加注 +84.00。72o：弃牌最优。交叉强度（案例 1 为 50）告诉你估错多少还安全。 |
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [Demo](https://andyzhang666666.github.io/commute-compare/) | 地图 App 只给一个数——「预计 42 分钟」。但通勤决策真正需要的是分布：地铁 40 分钟几乎不变，打车中位 30 分钟但堵车 70 分钟。均值更低的方案，迟到概率可能更高。 | 输入 2–6 个通勤方案（每个给「快 / 常见 / 慢」三个时间和单程花费），用 PERT 分布 + 蒙特卡洛模拟 2000 个月，输出月总时间、月总花费、迟到概率，以及「几点出门才能把迟到概率压到你能接受的水平」。两张图：到达时刻密度曲线（红线右边面积 = 迟到概率）、出门时间 vs 迟到概率曲线（拖阈值线看各方案最晚出门时间）。杭州 / 北京 / 上海 / 深圳四个预设，不限于某城市。用 PERT 而非正态，因为通勤时间天然右偏。 | 杭州金沙湖→西湖区，N=5,000 个月，上班 09:30、阈值 5%：地铁 P50 36.54h、¥264、08:32 出门、迟到 3.53%；打车 P50 29.07h、¥1,980、08:37 出门、迟到 4.99%。打车均值每月快 7.5 小时，但为同样准点率反而要更早出门，还贵 ¥1,716。 |

## 联系

[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
