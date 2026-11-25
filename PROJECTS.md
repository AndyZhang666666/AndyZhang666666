# 项目索引

[返回主页](README.zh-CN.md) · [English](PROJECTS.en.md)

按项目要解决的判断来浏览。Agent 台、RAG 台、偏爱实验室、随便局和安心装修的代码位于个人网站仓库内；其余工具在独立仓库维护。

## AI / Agent 与评测

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [Agent 执行评测台](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/agent-bench) · [体验](https://andyzhang666666.github.io/agent-bench/) | 响应超时后，查原操作与最终工单；审批、权限与幂等共同约束执行。 | 程序执行记录回放；Python / SQLite 后端可本地运行。 |
| [可信 RAG 实验台](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/rag-lab) · [体验](https://andyzhang666666.github.io/rag-lab/) | 导入个人资料，检索并选择引用、编辑答复；核对数字与日期、身份变化后的依据范围。 | TXT/Markdown/文字 PDF 本机解析与检索；草稿由用户确认，规则提示不等于语义认证；可选后端另行配置。 |
| [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [复核一条 2/5 的评语](https://andyzhang666666.github.io/llm-output-eval/?sample=e06&dimension=structure) · [用自己的文稿](https://andyzhang666666.github.io/llm-output-eval/workspace/) | 人工审阅、处理项与改稿对照；本版送评任务包和量表校准备忘。 | 自有文稿在本机审阅；6 个样本的 18 次历史输出另行回放；可选模型接口，原分保留。 |
| [Filing Eval](https://github.com/AndyZhang666666/filing-eval) · [体验](https://andyzhang666666.github.io/demos/filing-eval/) | 断言错误与重要遗漏分别回到原文核验。 | 28 条构造公告回放；人工记录独立保存。 |

## 生活与创新

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [安心装修](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/renovation) · [体验](https://andyzhang666666.github.io/renovation/) · [迭代](https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/main/renovation/CHANGELOG.md) | 看中的家具放得下吗？核对摆位净尺寸与送装总价。 | 虚构报价；离线 HTML、本机交接单与文本导出。 |
| [偏爱实验室](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom) · [体验](https://andyzhang666666.github.io/tasteroom/) | 编辑原创海报，对照同文同图的场景授权，明确确认可撤回的偏好记忆。 | 本机设计规则与导出；场景对照不写记忆，不调用模型或生图服务。 |
| [随便局](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/suibianju) · [体验](https://andyzhang666666.github.io/suibianju/) | 先确认底线，预演自愿调整，同版全员接受后形成决定。 | 3–5 位虚构角色的单人协商模拟。 |
| [有据 · Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [体验](https://andyzhang666666.github.io/grounded-choice/) | 保留经验分歧与适用条件，比较方案并导出决定。 | 原创模拟资料；不做实时搜索或自动电商比价。 |

## 增长与商业化

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [Bundle Lab](https://github.com/AndyZhang666666/bundle-lab) · [体验](https://andyzhang666666.github.io/bundle-lab/simulate/) | 自有商品/CSV 基线、两类人群账本、矩阵方案与冻结验证计划，后续观察核对原保本门槛。 | 内置合成订单或自有输入；未校准的条件毛利推演，不认证数据或因果收益。 |
| [Growth Experiment Lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [体验](https://andyzhang666666.github.io/growth-experiment-lab/) | 实验设计、反复查看风险、统计证据与发布判断。 | 固定种子模拟与合成台账；不自动批准上线。 |
| [Pricing Model Sim](https://github.com/AndyZhang666666/pricing-model-sim) · [体验](https://andyzhang666666.github.io/pricing-model-sim/) | 在同一批用户上比较付费机制、现金流和回本。 | 条件收入模型，价格与转化假设尚未校准。 |

## 日常决策与建模

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [通勤方案比较器](https://github.com/AndyZhang666666/commute-compare) · [体验](https://andyzhang666666.github.io/commute-compare/) | 一起比较成本、时间分布与迟到风险，用个人记录校准。 | 浏览器计算；无实时地图或路况接口。 |
| [扑克波动实验室](https://github.com/AndyZhang666666/poker-bankroll-sim) · [体验](https://andyzhang666666.github.io/poker-bankroll-sim/) | 分开表示额度不足停止、曾经达标与最终达标。 | 固定种子模型练习，保留残余余额。 |
| [扑克 EV 决策沙盘](https://github.com/AndyZhang666666/poker-ev-calculator) · [体验](https://andyzhang666666.github.io/poker-ev-calculator/) | 统一有效筹码口径，检查假设误差会不会改变选择。 | 单轮学习模型，不是 GTO 求解或真实胜率模型。 |
| [鱿鱼博弈实验室](https://github.com/AndyZhang666666/poker-squid-lab) · [体验](https://andyzhang666666.github.io/poker-squid-lab/) | 同一手牌对照三种规则，逐手回放结算，用挑战题核对判断。 | 本机规则沙盘与假设模拟，不是完整 GTO 或实际支付。 |

## 产品分析与历史版本

- [AI 产品拆解](https://github.com/AndyZhang666666/ai-product-teardowns)：可灵、豆包和文库 AI 的三篇阶段性分析，保留框架与实现推测的边界。
- [Creative Eval](https://github.com/AndyZhang666666/creative-eval)：Eval 第一版，保留 rubric 校准和历史输出。当前评审界面见 [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval)，两版样本不同，不合并成绩。

## 经历与研究

[官网](https://andyzhang666666.github.io/#work)另列工作经历、企业交付和研究主题。这些是案例说明，不把它们列成已公开的客户系统或源码仓库。各项目的使用权限以其自身许可证为准。

企业工具交付 · [看选品与人工核对](https://andyzhang666666.github.io/cases/agent-workflow/)

其他官网条目：[个人投研工作流](https://andyzhang666666.github.io/#project-research-agent) · [内容获客案例](https://andyzhang666666.github.io/#project-content) · [扑克玩家类型测试（外站介绍）](https://andyzhang666666.github.io/#project-poker-quiz)。

[跨语言搜索案例](https://andyzhang666666.github.io/#evidence-search) · [同款、近似款与待核实款](https://andyzhang666666.github.io/#evidence-matching)

## 最近交付 · 2026

- **11.15**　安心装修。旧缓存让新作品卡片出现后又消失，修复后从官网重新走通入口。 [发布记录](https://github.com/AndyZhang666666/AndyZhang666666.github.io/pull/13)
- **11.13**　Eval。手机用户核对引文后，可以回到同一条评语继续复核。 [发布记录](https://github.com/AndyZhang666666/llm-output-eval/pull/6)
- **11.13**　Bundle。可以在折扣矩阵里预演一个方案，再决定是否采用。 [发布记录](https://github.com/AndyZhang666666/bundle-lab/pull/5)

## 工作与其他作品

在山海星辰做创作 Agent 与可复用 Skill，在百度参与文库 AI 产品，在 Keeta 做海外用户增长。在 Keeta 做跨语言搜菜时，一个具体问题是：阿语音译多找回一道菜，要怎么判断有没有错配？

<details>
<summary>更多经历与研究背景</summary>

在 Keeta 做分层补贴实验，在理想汽车参与智能座舱交互，在 Revolut 参与订阅权益与升级流程。UCL 硕士期间研究标普 500 订单流与日内交易；Bristol 本科毕设把运动姿态监测与手机端反馈结合起来。

</details>

[工作经历](https://andyzhang666666.github.io/#work) · [Keeta 跨语言搜索案例](https://andyzhang666666.github.io/#evidence-search) · [企业工具交付](https://andyzhang666666.github.io/cases/agent-workflow/) · [Agent 执行评测](https://andyzhang666666.github.io/agent-bench/)

产品设计图和操作记录 · [Eval](docs/editorial/projects/eval.md) · [TasteRoom](docs/editorial/projects/taste.md) · [Bundle](docs/editorial/projects/bundle.md) · [RAG](docs/editorial/projects/rag.md)

[双语菜单检索](https://andyzhang666666.github.io/studio/menu/)
