# 项目索引

[返回主页](README.md) · [English](PROJECTS.en.md)

按项目要解决的判断来浏览。Agent 台、RAG 台、偏爱实验室和随便局的代码位于个人网站仓库内；其余工具在独立仓库维护。

## AI / Agent 与评测

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [Agent 执行评测台](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/agent-bench) · [体验](https://andyzhang666666.github.io/agent-bench/) | 响应超时后，查原操作与最终工单；审批、权限与幂等共同约束执行。 | 程序执行记录回放；Python / SQLite 后端可本地运行。 |
| [可信 RAG 实验台](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/rag-lab) · [体验](https://andyzhang666666.github.io/rag-lab/) | 先限定适用资料，再检查检索、引用、冲突和资料不足。 | 公开资料的 BM25 检索与规则摘录；本地 API 另有范围检查。 |
| [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval) · [体验](https://andyzhang666666.github.io/llm-output-eval/) | 逐维评分、引用定位与独立人工复核。 | 6 条样本的 18 次历史输出；可选配置模型接口。 |
| [Filing Eval](https://github.com/AndyZhang666666/filing-eval) · [体验](https://andyzhang666666.github.io/demos/filing-eval/) | 断言错误与重要遗漏分别回到原文核验。 | 28 条构造公告回放；人工记录独立保存。 |

## 生活与创新

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [偏爱实验室](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom) · [体验](https://andyzhang666666.github.io/tasteroom/) | 单变量审美对照、范围授权、可撤回的偏好记忆。 | 原创海报与本地规则；不调用模型或生图服务。 |
| [随便局](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/suibianju) · [体验](https://andyzhang666666.github.io/suibianju/) | 先确认底线，预演自愿调整，同版全员接受后形成决定。 | 3–5 位虚构角色的单人协商模拟。 |
| [有据 · Grounded Choice](https://github.com/AndyZhang666666/grounded-choice) · [体验](https://andyzhang666666.github.io/grounded-choice/) | 保留经验分歧与适用条件，比较方案并导出决定。 | 原创模拟资料；不做实时搜索或自动电商比价。 |

## 增长与商业化

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [Bundle Lab](https://github.com/AndyZhang666666/bundle-lab) · [体验](https://andyzhang666666.github.io/bundle-lab/) | 从共购候选进入两类人群账本，再提出验证计划。 | 合成订单和未校准的行为假设。 |
| [Growth Experiment Lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [体验](https://andyzhang666666.github.io/growth-experiment-lab/) | 实验设计、反复查看风险、统计证据与发布判断。 | 固定种子模拟与合成台账；不自动批准上线。 |
| [Pricing Model Sim](https://github.com/AndyZhang666666/pricing-model-sim) · [体验](https://andyzhang666666.github.io/pricing-model-sim/) | 在同一批用户上比较付费机制、现金流和回本。 | 条件收入模型，价格与转化假设尚未校准。 |

## 日常决策与建模

| 项目 | 问题与机制 | 运行方式 |
| --- | --- | --- |
| [通勤方案比较器](https://github.com/AndyZhang666666/commute-compare) · [体验](https://andyzhang666666.github.io/commute-compare/) | 一起比较成本、时间分布与迟到风险，用个人记录校准。 | 浏览器计算；无实时地图或路况接口。 |
| [扑克波动实验室](https://github.com/AndyZhang666666/poker-bankroll-sim) · [体验](https://andyzhang666666.github.io/poker-bankroll-sim/) | 分开表示额度不足停止、曾经达标与最终达标。 | 固定种子模型练习，保留残余余额。 |
| [扑克 EV 决策沙盘](https://github.com/AndyZhang666666/poker-ev-calculator) · [体验](https://andyzhang666666.github.io/poker-ev-calculator/) | 统一有效筹码口径，检查假设误差会不会改变选择。 | 单轮学习模型，不是 GTO 求解或真实胜率模型。 |

## 产品分析与历史版本

- [AI 产品拆解](https://github.com/AndyZhang666666/ai-product-teardowns)：可灵、豆包和文库 AI 的三篇阶段性分析，保留框架与实现推测的边界。
- [Creative Eval](https://github.com/AndyZhang666666/creative-eval)：Eval 第一版，保留 rubric 校准和历史输出。当前评审界面见 [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval)，两版样本不同，不合并成绩。

## 经历与研究

[官网](https://andyzhang666666.github.io/#work)另列工作经历、企业交付和研究主题。这些是案例说明，不把它们列成已公开的客户系统或源码仓库。各项目的使用权限以其自身许可证为准。
