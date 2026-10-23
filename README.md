# Andy Zhang (张千羽)

AI Product Manager. I work on agent workflows, prompt-asset platforms and evaluation systems, and on user growth and monetization.

- **AI product design** — From a business scenario to a shipped AI feature: agent workflow design, reusable prompt-asset management, and evaluation systems that tell you whether the new version is actually better. Work closely with algorithm teams to take AI products from 0 to 1 and scale them.
- **Data-driven, closed-loop** — SQL/Python for analysis and strategy validation; A/B testing, event-tracking attribution and funnel decomposition to break down business problems, find growth paths that can be shipped, and verify them.
- **Growth & monetization** — From user-scenario insight to paid-conversion path design: spotting high-value scenarios, designing differentiated experiences, hands-on with subscription rollout and promotion optimization. Overseas market experience; English as a working language.

The projects below are what these three look like in practice. **Try the demos → [andyzhang666666.github.io](https://andyzhang666666.github.io)** — interactive projects, nothing to install.

## Projects

### AI evaluation

| Project | Problem | What I built | Result |
|---|---|---|---|
| [creative-eval](https://github.com/AndyZhang666666/creative-eval) · [demo](https://andyzhang666666.github.io) | A content team gets 200 AI-generated script fragments a day; QA is still three people reading. No consistent way to say "v2 is better than v1". | An LLM judge that scores short-drama scripts on 5 fixed dimensions (hook, pacing, dialogue, persona, structure), each with written 1/3/5 anchors, and must quote evidence from the text. A 40-item golden set with human labels, and a validation suite: run-to-run stability, agreement with humans, length and order bias. | 93.1% within-±1 agreement with human raters. v1 judge was +0.38 too lenient; adding score anchors brought it to +0.23. |
| [llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval) · [demo](https://andyzhang666666.github.io/llm-output-eval/) | Compare generated text using evidence, not just an overall score. | No-key historical replay: source evidence, truncated/full-text comparison, separately labeled bad-case CSV and judge validation. Optional BYO-key evaluation remains available. | 6 replay samples, 18 recorded runs. Historical validation on 30 author-labeled samples: Spearman ρ 0.93. No new model calls in this update. |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) | AI summaries of listed-company filings occasionally turn 120M into 1.2B or invent a sentence. Subjective scoring can't catch that. | Claim-level fact checking: split the summary into claims, match each back to the filing, label supported / contradicted / unsupported, then check key-fact coverage. Tested on 20 main samples plus 8 adversarial ones with planted errors and prompt injections. | 11/11 planted errors caught, 0/4 false positives, 5/5 injections held. |

### Growth & monetization

| Project | Problem | What I built | Result |
|---|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [demo](https://andyzhang666666.github.io/growth-experiment-lab/) | Plan sample size, resist early stopping and distinguish statistical evidence from a rollout decision. | Sample-size design, peeking simulation and effect intervals. Revenue scenarios are conditional, not guaranteed profit; guardrails, costs and experiment validity must be checked before rollout. | Historical zero-effect simulation: stopping at the first p<0.05 raised false positives from 4.95% to 22.45%. |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [demo](https://andyzhang666666.github.io/pricing-model-sim/) | Compare pricing mechanisms under explicit assumptions rather than comparing revenue totals alone. | Retention, price and conversion scenarios across unlock, subscription and hybrid models. Conclusions and tables share per-new-user metrics; sensitivity sweeps expose ranking changes. | Four synthetic cases; findings are conditional on uncalibrated retention and conversion assumptions, not an optimal real-world price. |

### Commerce & product analysis

| Project | Problem | What I built | Result |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [demo](https://andyzhang666666.github.io/bundle-lab/) | Turn co-purchase observations into testable bundle hypotheses without claiming causality. | Explore synthetic order profiles, discover combinations, compare adoption and discount scenarios, and export a bounded recommendation. Shared portions and party-size definitions remain alternative explanations. | Historical synthetic validation recovered 5/5 planted bundles. Current release fixes deployment links and missing group-share statistics; it does not prove sales uplift. |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | Most AI product reviews are feature lists. | Three teardowns (Kling, Doubao, Wenku AI) against one fixed 6-dimension framework: capability boundary, failure handling, how effect is measured, agentic potential, cost and latency, and what I'd do next as PM. | The framework is the reusable part. |

### Poker & Everyday Decisions

| Project | Problem | What I built | Result |
|---|---|---|---|
| [Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [demo](https://andyzhang666666.github.io/grounded-choice/) | Saved travel tips and product reviews pile up, but conflicting opinions and personal constraints still make the final choice hard. | A two-scenario decision workflow for a western Sichuan trip and a robot vacuum: traceable simulated sources, consensus and disagreement, hard-constraint flags, trade-off comparison, user-controlled selection and an exportable decision card. | A working portfolio demo. All source material and comments are simulated; it does not perform live search or price comparison. |
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

下面的项目是这三条能力的具体样子。**在线 Demo → [andyzhang666666.github.io](https://andyzhang666666.github.io)**，打开即可体验。

## 项目

### AI 效果评估

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [creative-eval](https://github.com/AndyZhang666666/creative-eval) · [Demo](https://andyzhang666666.github.io) | 内容团队用 AI 一天能出 200 条剧本片段，但判断质量的还是那几个人。新版 prompt 好不好，只能靠「感觉顺一点」。 | 一个短剧剧本的 LLM 评分裁判：5 个固定维度（开场钩子、节奏、对白、人设、结构），每档写死 1/3/5 分锚点，每个分数必须引用原文证据。配一套 40 条人工标注的金标集，和一套校验脚本：同一条连跑 3 次稳不稳、和人工标注一不一样、会不会看长度和顺序给分。 | 与人工标注 ±1 分一致率 93.1%。第一版裁判偏松 +0.38，加打分基准后降到 +0.23。 |
| [llm-output-eval](https://github.com/AndyZhang666666/llm-output-eval) · [Demo](https://andyzhang666666.github.io/llm-output-eval/) | 比较生成文本，需要看证据和波动，不只看一个总分。 | 无需 Key 的历史评测回放，包含原文证据、截断稿/完整稿对照、独立标记的低分 CSV 和裁判校验。保留自带接口的真实评测能力。 | 回放 6 个样本的 18 次原有输出；原 30 条作者标注集的 Spearman ρ 为 0.93。本轮未重新调用模型。 |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) | AI 把上市公司公告压成摘要，会把 1.2 亿写成 12 亿、会凭空多一句。主观打分抓不住这类错。 | 断言级事实核查：把摘要拆成一条条断言，逐条回原文比对，标「支持 / 矛盾 / 无依据」，再查关键事实覆盖率。20 条主集 + 8 条对抗样本（故意植入错误和提示注入）。 | 植入错误检出 11/11、干净样本误报 0/4、提示注入 5/5 守住。 |

### 增长与商业化

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [Demo](https://andyzhang666666.github.io/growth-experiment-lab/) | 规划样本、控制提前停止风险，并将统计证据与全量决策分开。 | 样本量设计、偷看风险模拟及效果区间；收入情景不是保底利润，上线前另核对护栏、成本与实验有效性。 | 原有零效应模拟中，每天偷看且一显著就停，假阳性率从 4.95% 涨到 22.45%。 |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [Demo](https://andyzhang666666.github.io/pricing-model-sim/) | 在明确假设下比较付费机制，而不是只比收入总额。 | 调整留存、价格和转化，比较解锁、订阅与混合机制；结论和表格统一每名新增用户口径，敏感性分析寻找排序变化条件。 | 4 个合成案例；结论受未校准留存与转化假设限制，不作为真实最优定价建议。 |

### 电商与产品分析

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [Demo](https://andyzhang666666.github.io/bundle-lab/) | 从共购观察提出套餐假设，不把相关性直接当作原因。 | 用合成订单看画像、挖组合、比较采纳率与折扣下的收益边界，再导出建议。共享份量和人数口径仍需核查。 | 原有合成校验召回 5/5 预埋组合；本轮修复部署链接与统计缺失，不宣称已验证销售增长。 |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | 多数 AI 产品评测是功能清单。 | 用同一套六维框架拆解可灵、豆包、文库 AI：能力边界、答错时怎么办、效果怎么衡量、智能体潜力、成本时延、如果我是 PM 下一步做什么。 | 框架是可复用的部分。 |

### 德州扑克与日常决策

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [有据 Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [Demo](https://andyzhang666666.github.io/grounded-choice/) | 收藏的攻略和测评越多，观点越容易冲突；还得自己判断哪些经验适用、哪些方案违反硬约束。 | 用川西旅行和扫地机器人两个场景演示一条决策流程：模拟材料可追溯、共识和分歧不抹平、约束冲突明示、方案代价并排比较，最终由用户选并导出决策卡。 | 可交互的作品演示；资料与评论均为模拟内容，不接入实时搜索或电商比价。 |
| [poker-bankroll-sim](https://github.com/AndyZhang666666/poker-bankroll-sim) · [Demo](https://andyzhang666666.github.io/poker-bankroll-sim/) | 「带 20 个买入」是圈子里流传已久的经验规则，大致对，但没人告诉你这 20 个买入对应的破产概率到底是 5% 还是 40%，也没人告诉你胜率从 52% 掉到 50% 时会发生什么。 | 输入起始资金、每次买入金额、胜率、方差，蒙特卡洛跑 100/500/1,000 场，输出资金曲线（10 条模拟路径 + 中位数 + p10/p90 分位带）、破产概率、达标概率、最大回撤。三个预设场景（保守 / 平衡 / 激进），附一份解析解（连续布朗运动的首次穿越）用来交叉验证模拟结果。 | 10,000 次模拟（固定种子）：保守型破产率 2.64%（达标率 75.60%），平衡型 29.61%，激进型 42.69%。买入从本金 2.5% 提到 5%，破产率从 2.6% 跳到 29.6%——是数量级差别，不是线性放大。 |
| [poker-ev-calculator](https://github.com/AndyZhang666666/poker-ev-calculator) · [Demo](https://andyzhang666666.github.io/poker-ev-calculator/) | 市面上的 EV 计算器要么太复杂（要输入精确对手范围），要么太简单（只算底池赔率，不管对手是谁、做了什么动作）。这个工具取中间。 | 输入三个可观测项——手牌强度、对手类型、对手动作——估胜率，把弃牌 / 跟注 / 加注三个决策的期望收益摆在一起比。柱状图对比三个决策，最优项高亮并给理由，敏感性 tab 把手牌强度 0→100 扫一遍，找「跟注变对」的交叉点。8 个经典场景一键填充，169 种起手牌强度查表。关键修正：加注 EV 用「被跟注后的胜率」而非原始胜率——对手愿意跟你的加注说明他范围变强了，少这层折价加注会被系统性高估。 | 8/8 案例与预期一致。翻牌前 AA vs 加注：加注 EV +42.50 最优。转牌顺子听牌：跟注 +100.00 优于加注 +84.00。72o：弃牌最优。交叉强度（案例 1 为 50）告诉你估错多少还安全。 |
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [Demo](https://andyzhang666666.github.io/commute-compare/) | 地图 App 只给一个数——「预计 42 分钟」。但通勤决策真正需要的是分布：地铁 40 分钟几乎不变，打车中位 30 分钟但堵车 70 分钟。均值更低的方案，迟到概率可能更高。 | 输入 2–6 个通勤方案（每个给「快 / 常见 / 慢」三个时间和单程花费），用 PERT 分布 + 蒙特卡洛模拟 2000 个月，输出月总时间、月总花费、迟到概率，以及「几点出门才能把迟到概率压到你能接受的水平」。两张图：到达时刻密度曲线（红线右边面积 = 迟到概率）、出门时间 vs 迟到概率曲线（拖阈值线看各方案最晚出门时间）。杭州 / 北京 / 上海 / 深圳四个预设，不限于某城市。用 PERT 而非正态，因为通勤时间天然右偏。 | 杭州金沙湖→西湖区，N=5,000 个月，上班 09:30、阈值 5%：地铁 P50 36.54h、¥264、08:32 出门、迟到 3.53%；打车 P50 29.07h、¥1,980、08:37 出门、迟到 4.99%。打车均值每月快 7.5 小时，但为同样准点率反而要更早出门，还贵 ¥1,716。 |

## 联系

[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
