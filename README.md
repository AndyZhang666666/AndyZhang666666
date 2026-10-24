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
| [文本评测工作台 / Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [demo](https://andyzhang666666.github.io/llm-output-eval/) · [iterations](https://andyzhang666666.github.io/llm-output-eval/iteration/) | Compare generated text with inspectable evidence and check the judge itself. | One project, two iterations: V1 creative-eval established scoring anchors; V2 adds no-key replay, repeated comparisons, bad-case export and judge validation. Both source repositories remain available. | V1: 40 constructed cases, 32 author-labeled. V2: a separate 30 author-labeled cases; replay shows 18 recorded runs for 6 examples. Different datasets are not pooled or claimed as proof of improvement. |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) · [demo](https://andyzhang666666.github.io/demos/filing-eval/) | Trace each summary claim to source evidence, including missing facts and disputed scope. | A no-key evidence desk for 28 synthetic historical cases: quote location, separate omissions/disputes, local review notes and JSON export. | Historical main set: 11/11 errors detected, 0/4 false positives; labels lack independent human review. Six new holdout candidates are unrun, not added to scores. |

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
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [demo](https://andyzhang666666.github.io/commute-compare/) | Compare commute time/cost without first knowing the worst-case journey. | Start with typical time and cost, then replace estimates with personal duration records. Show per-route provenance, sample limits, observed-rate intervals, departure trade-offs and exportable decisions. | No map or model API. Empirical resampling is conditional on the records; zero observed late trips and more simulations do not guarantee future punctuality. Drafts stay local. |

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
| [文本评测工作台 / Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [Demo](https://andyzhang666666.github.io/llm-output-eval/) · [迭代记录](https://andyzhang666666.github.io/llm-output-eval/iteration/) | 用原文证据比较内容质量，也检查裁判自己的偏差与波动。 | 一个项目、两轮迭代：V1 creative-eval 建立评分锚点，V2 补齐免 Key 回放、重复对照、低分导出和裁判校验。两个源码仓库均保留。 | V1 为 40 条构造样本、32 条作者标注；V2 是另一套 30 条作者标注，回放其中 6 条的 18 次历史输出。不混算，不宣称已证明新版质量提升。 |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) · [Demo](https://andyzhang666666.github.io/demos/filing-eval/) | 从摘要断言回到原文，分清写错、无据、遗漏和主体争议。 | 28 条模拟公告历史回放，支持引文定位、本地复核与 JSON 导出，无需 Key。 | 历史主集检出 11/11、误报 0/4；标签尚未完成独立人工复核。新增 6 条候选留出样本未调用模型，不计入成绩。 |

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
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [Demo](https://andyzhang666666.github.io/commute-compare/) | 不用先猜“最慢会多久”，也能比较通勤时间与费用。 | 常见耗时和费用即可开始，再用自己的实际记录替换估算；展示来源、样本不足、观测比例区间、出门权衡并导出决策。 | 不接地图或模型接口；经验重采样受样本范围限制，0 次观测迟到不代表真实风险为 0。记录和草稿仅存本机。 |

## 联系

[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
