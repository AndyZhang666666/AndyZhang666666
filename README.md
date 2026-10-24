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
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [demo](https://andyzhang666666.github.io/growth-experiment-lab/) | Separate experiment evidence from rollout permission. | Export design plans and readouts; run cancellable Worker simulations; require manual validity, guardrail and business-threshold checks. Input changes invalidate confirmations. | Synthetic cases use one draw each, not outcome-based resampling. Non-significance is not no effect; revenue scenarios are not guaranteed profit. |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [demo](https://andyzhang666666.github.io/pricing-model-sim/) | Compare pricing mechanisms under explicit assumptions rather than comparing revenue totals alone. | Retention, price and conversion scenarios across unlock, subscription and hybrid models. Conclusions and tables share per-new-user metrics; sensitivity sweeps expose ranking changes. | Four synthetic cases; findings are conditional on uncalibrated retention and conversion assumptions, not an optimal real-world price. |

### Commerce & product analysis

| Project | Problem | What I built | Result |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [demo](https://andyzhang666666.github.io/bundle-lab/) | Turn co-purchase observations into testable bundle hypotheses without claiming causality. | Explore synthetic order profiles, discover combinations, compare adoption and discount scenarios, and export a bounded recommendation. Shared portions and party-size definitions remain alternative explanations. | Historical synthetic validation recovered 5/5 planted bundles. Current release fixes deployment links and missing group-share statistics; it does not prove sales uplift. |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | Most AI product reviews are feature lists. | Three teardowns (Kling, Doubao, Wenku AI) against one fixed 6-dimension framework: capability boundary, failure handling, how effect is measured, agentic potential, cost and latency, and what I'd do next as PM. | The framework is the reusable part. |

### Everyday AI experiments

| Project | Problem | What I built | Result |
|---|---|---|---|
| [Suibianju · 随便局](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/suibianju) · [demo](https://andyzhang666666.github.io/suibianju/) | “Anything is fine” hides constraints; a majority vote should not override someone's hard limit. | Opt-in budget proposals, side-effect-free draft previews, 3–5 simulated roles, unanimous versioned agreement and a public decision receipt. | A working, no-key single-person simulation. People and restaurants are fictional; no live rooms, booking, model calls or user-impact claims. |
| [TasteRoom · 偏爱实验室](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom) · [demo](https://andyzhang666666.github.io/tasteroom/) | Liking a whole poster does not identify which parameter or context a preference belongs to. | Single-variable comparisons, neither-choice, explicit scope consent, contextual memory, reversible edits and style-brief / SVG export. | A working local-rule demo. Clues stay distinct from explicit rules; no live model, image generation, calibrated preference accuracy or adoption claims. |

### Poker & Everyday Decisions

| Project | Problem | What I built | Result |
|---|---|---|---|
| [Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [demo](https://andyzhang666666.github.io/grounded-choice/) | Saved travel tips and product reviews pile up, but conflicting opinions and personal constraints still make the final choice hard. | A two-scenario decision workflow for a western Sichuan trip and a robot vacuum: traceable simulated sources, consensus and disagreement, hard-constraint flags, trade-off comparison, user-controlled selection and an exportable decision card. | A working portfolio demo. All source material and comments are simulated; it does not perform live search or price comparison. |
| [poker-bankroll-sim](https://github.com/AndyZhang666666/poker-bankroll-sim) · [demo](https://andyzhang666666.github.io/poker-bankroll-sim/) | Reaching a target once is not the same as finishing above it. | A seeded synthetic sandbox separating insufficient-stake stopping, zero balance, ever reaching a goal and terminal success; retain residual balances, scan one variable at a time and export provenance. | Reproducible model scenarios, not player outcomes or financial predictions. Sampling intervals do not include model uncertainty. |
| [poker-ev-calculator](https://github.com/AndyZhang666666/poker-ev-calculator) · [demo](https://andyzhang666666.github.io/poker-ev-calculator/) | Does the preferred action change if a strength assumption is wrong? | Use effective stakes consistently for pot odds and EV; compare actions across a discrete strength range; restore local drafts and export a versioned decision record with assumptions. | Eight preset regression cases plus boundary and browser checks. A single-street learning model, not calibrated equity, GTO or betting advice. |
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
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [Demo](https://andyzhang666666.github.io/growth-experiment-lab/) | 将实验设计、统计证据与上线许可分开。 | 设计计划和决策记录可导出；偷看模拟可取消；人工核对有效性、护栏与预设业务门槛，修改输入使确认失效。 | 合成台账每例只抽一次，不为结论挑数据。不显著不等于无效，收入情景不是保底利润。 |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [Demo](https://andyzhang666666.github.io/pricing-model-sim/) | 在明确假设下比较付费机制，而不是只比收入总额。 | 调整留存、价格和转化，比较解锁、订阅与混合机制；结论和表格统一每名新增用户口径，敏感性分析寻找排序变化条件。 | 4 个合成案例；结论受未校准留存与转化假设限制，不作为真实最优定价建议。 |

### 电商与产品分析

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [Demo](https://andyzhang666666.github.io/bundle-lab/) | 从共购观察提出套餐假设，不把相关性直接当作原因。 | 用合成订单看画像、挖组合、比较采纳率与折扣下的收益边界，再导出建议。共享份量和人数口径仍需核查。 | 原有合成校验召回 5/5 预埋组合；本轮修复部署链接与统计缺失，不宣称已验证销售增长。 |
| [ai-product-teardowns](https://github.com/AndyZhang666666/ai-product-teardowns) | 多数 AI 产品评测是功能清单。 | 用同一套六维框架拆解可灵、豆包、文库 AI：能力边界、答错时怎么办、效果怎么衡量、智能体潜力、成本时延、如果我是 PM 下一步做什么。 | 框架是可复用的部分。 |

### 生活 AI 实验

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [随便局](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/suibianju) · [Demo](https://andyzhang666666.github.io/suibianju/) | “随便”掩盖底线，多数票不应该替少数人决定。 | 自愿预算建议、无副作用草稿预演、3–5 位模拟角色、同版全员接受、公共决定单复制与下载。 | 可直接操作的免 Key 单人模拟；人物和餐厅虚构，没有真实房间、订位、模型调用或用户效果宣称。 |
| [TasteRoom · 偏爱实验室](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom) · [Demo](https://andyzhang666666.github.io/tasteroom/) | 喜欢整张海报，不能直接判断喜欢哪个参数、适用于哪个场景。 | 单变量对照、都不选、范围授权、场景记忆、记忆操作撤回，以及偏好说明书与 SVG 导出。 | 可操作的本地规则 Demo，线索和明确规则分开；没有真实模型、生图、偏好准确率或采用率宣称。 |

### 德州扑克与日常决策

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [有据 Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [Demo](https://andyzhang666666.github.io/grounded-choice/) | 收藏的攻略和测评越多，观点越容易冲突；还得自己判断哪些经验适用、哪些方案违反硬约束。 | 用川西旅行和扫地机器人两个场景演示一条决策流程：模拟材料可追溯、共识和分歧不抹平、约束冲突明示、方案代价并排比较，最终由用户选并导出决策卡。 | 可交互的作品演示；资料与评论均为模拟内容，不接入实时搜索或电商比价。 |
| [poker-bankroll-sim](https://github.com/AndyZhang666666/poker-bankroll-sim) · [Demo](https://andyzhang666666.github.io/poker-bankroll-sim/) | 曾经达到目标，不等于最终守住目标。 | 固定种子的合成沙盘，区分额度不足停止、余额归零、曾经达标与最终达标；保留剩余余额，单变量扫描，并导出带出处的比较记录。 | 可复现的模型情景，不是真实玩家结果或资金预测。抽样区间不覆盖模型假设误差。 |
| [poker-ev-calculator](https://github.com/AndyZhang666666/poker-ev-calculator) · [Demo](https://andyzhang666666.github.io/poker-ev-calculator/) | 强度假设估错一点，较优行动会不会改变？ | 用有效筹码统一赔率与 EV；逐点检查强度区间的行动切换；本机草稿恢复，导出带假设与模型版本的决策记录。 | 保留 8 个预设回归案例，新增边界和浏览器验证。单轮学习模型，不是已校准胜率、GTO 或下注建议。 |
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [Demo](https://andyzhang666666.github.io/commute-compare/) | 不用先猜“最慢会多久”，也能比较通勤时间与费用。 | 常见耗时和费用即可开始，再用自己的实际记录替换估算；展示来源、样本不足、观测比例区间、出门权衡并导出决策。 | 不接地图或模型接口；经验重采样受样本范围限制，0 次观测迟到不代表真实风险为 0。记录和草稿仅存本机。 |

## 联系

[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
