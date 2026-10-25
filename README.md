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
| [文本评测工作台 / Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [demo](https://andyzhang666666.github.io/llm-output-eval/) · [iterations](https://andyzhang666666.github.io/llm-output-eval/iteration/) | Review the evidence behind a judge’s score. | Locate quotes in source text, isolate human notes by run and export original scores with review decisions. No-key replay; optional API requests are cancellable and keys are not persisted. | V1: 40 constructed cases, 32 author-labeled. V2: separate 30 author-labeled cases; replay has 18 stored runs for 6 examples. Current workflow verified locally and live with mocked API responses; historical model metrics were not rerun. |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) · [demo](https://andyzhang666666.github.io/demos/filing-eval/) | Check wrong claims and important omissions separately. | Review 28 synthetic historical cases without default agreement, continue pending claims or coverage checks, and export source, summary, original judgments and human reasoning. | 102 historical claims are inspectable. Historical main set: 11/11 errors detected, 0/4 false positives; labels lack independent human review. Six holdout candidates remain unrun; no new model-effect claim. |

### Growth & monetization

| Project | Problem | What I built | Result |
|---|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [demo](https://andyzhang666666.github.io/growth-experiment-lab/) | Separate experiment evidence from rollout permission. | Export design plans and readouts; run cancellable Worker simulations; require manual validity, guardrail and business-threshold checks. Input changes invalidate confirmations. | Synthetic cases use one draw each, not outcome-based resampling. Non-significance is not no effect; revenue scenarios are not guaranteed profit. |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [demo](https://andyzhang666666.github.io/pricing-model-sim/) | Compare mechanisms with conserved user pools and explicit assumptions. | Monthly unlock/subscription/exit traces; one-field sweeps preserve other inputs; discounted payback, ties, zero prices, local drafts and reproducible export. | Four synthetic cases; hand checks, invariants and live browser flows verified. Retention and conversion remain uncalibrated; no optimal-price or business-return claim. |

### Commerce & product analysis

| Project | Problem | What I built | Result |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [demo](https://andyzhang666666.github.io/bundle-lab/) | Separate new-purchase margin from discounts to existing full-basket customers. | All-candidate discovery, a reconciled two-population ledger and break-even model, local scenario recovery, linked recommendations and evidence exports with a validation plan. Model polish remains an unverified draft. | Hand checks, economic boundaries and six-route live workflows verified. Synthetic orders and uncalibrated adoption assumptions do not prove causal sales uplift or net profit. |
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
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [demo](https://andyzhang666666.github.io/commute-compare/) | Make commute trade-offs without confusing estimates and observations. | Confirm editable inputs, resample personal duration records, preview/commit departure thresholds and export evidence. Removing a route leaves others unchanged; invalid saved drafts are preserved. | Four synthetic city presets, regression checks and live browser flows verified. No map/model API or future punctuality guarantee; sparse records and return-trip assumptions remain visible. |

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
| [文本评测工作台 / Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [Demo](https://andyzhang666666.github.io/llm-output-eval/) · [迭代记录](https://andyzhang666666.github.io/llm-output-eval/iteration/) | 核对分数背后的证据，而不只看总分。 | 点击引用定位原文，按运行隔离人工复核，导出保留原始分数。免 Key 回放；可选接口可取消、Key 不持久保存。 | V1 为40条构造样本、32条作者标注；V2 为另一套30条作者标注，回放6条的18次历史输出。本地/线上流程与模拟接口通过；历史模型指标未重跑。 |
| [filing-eval](https://github.com/AndyZhang666666/filing-eval) · [Demo](https://andyzhang666666.github.io/demos/filing-eval/) | 把错句与关键遗漏分开核验。 | 28条模拟公告回放，不默认同意历史裁判；继续未复核断言或覆盖项，导出原文、摘要、原始判断和人工依据。 | 102条历史断言可核对。历史主集检出11/11、误报0/4；标签未独立人工复核。6条候选留出未运行，不宣称新增模型效果。 |

### 增长与商业化

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [growth-experiment-lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [Demo](https://andyzhang666666.github.io/growth-experiment-lab/) | 将实验设计、统计证据与上线许可分开。 | 设计计划和决策记录可导出；偷看模拟可取消；人工核对有效性、护栏与预设业务门槛，修改输入使确认失效。 | 合成台账每例只抽一次，不为结论挑数据。不显著不等于无效，收入情景不是保底利润。 |
| [pricing-model-sim](https://github.com/AndyZhang666666/pricing-model-sim) · [Demo](https://andyzhang666666.github.io/pricing-model-sim/) | 在人群守恒、假设明确的基础上比较三种付费机制。 | 逐月解锁/订阅/流失轨迹；保留其他输入的单字段扫描；折现回本、并列、零价格、本机草稿与可复现导出。 | 4 个合成案例，手算、守恒与线上流程已验收；留存转化未经校准，不声称真实最优价格或业务收益。 |

### 电商与产品分析

| 项目 | 解决什么问题 | 做了什么 | 结果 |
|---|---|---|---|
| [bundle-lab](https://github.com/AndyZhang666666/bundle-lab) · [Demo](https://andyzhang666666.github.io/bundle-lab/) | 分开核算新增购买毛利与既有整套顾客领取折扣的损失。 | 全候选发现、两类人群账本、同源平衡点、本机假设恢复、建议与依据导出及后续验证计划；模型润色独立标记未核对。 | 手算、收益边界与线上六页流程已验收；合成数据与未校准采纳率不证明因果增长或净利润。 |
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
| [commute-compare](https://github.com/AndyZhang666666/commute-compare) · [Demo](https://andyzhang666666.github.io/commute-compare/) | 比较通勤取舍，同时分清估算与观测。 | 确认数字输入，以实际记录校准，预览/提交出门阈值并导出依据。删除路线不让其他结果漂移；损坏草稿不会自动覆盖。 | 四城模拟预设、原有回归及线上浏览器流程通过；不接地图或模型，不保证未来准点，样本不足与往返假设明确保留。 |

## 联系

[GitHub](https://github.com/AndyZhang666666) · [Demo 站](https://andyzhang666666.github.io)
