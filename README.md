<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile-dark.svg">
  <img src="assets/profile-light.svg" alt="Agent / Evaluation / Growth · a compact decision trace" width="100%">
</picture>

# 张千羽 · Andy Zhang

**AI 产品经理，做 Agent、效果评测和商业增长。**

我把业务问题做成可操作的产品，再核对它是否解决了问题。下面四个作品，可以直接体验我的设计取舍。

[官网与完整体验](https://andyzhang666666.github.io/) · [产品简历](https://andyzhang666666.github.io/assets/resume.pdf) · [English](README.en.md) · [全部项目](PROJECTS.md)

## 从这里开始

<table>
<tr>
<td width="50%" valign="top">
<p><strong>Agent 执行评测台</strong><br>响应丢失后，先核对原操作。</p>
<a href="https://andyzhang666666.github.io/agent-bench/"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/assets/agent-preview.jpg"><img src="docs/assets/agent-replay.gif" alt="Agent 执行评测台：响应丢失后，先核对原操作。" width="100%"></picture></a>
<p>程序示例 · 不调用 AI<br><a href="https://andyzhang666666.github.io/agent-bench/">体验</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/agent-bench">源码与设计</a></p>
</td>
<td width="50%" valign="top">
<p><strong>Eval Lab</strong><br>分数之后，回到原文与人工复核。</p>
<a href="https://andyzhang666666.github.io/llm-output-eval/"><img src="docs/assets/eval-preview.jpg" alt="Eval Lab：分数之后，回到原文与人工复核。" width="100%"></a>
<p>历史输出 · 原分保留<br><a href="https://andyzhang666666.github.io/llm-output-eval/">体验</a> · <a href="https://github.com/AndyZhang666666/llm-output-eval">源码与设计</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><strong>偏爱实验室</strong><br>比较设计，再决定偏爱记在哪里。</p>
<a href="https://andyzhang666666.github.io/tasteroom/"><img src="docs/assets/taste-preview.jpg" alt="偏爱实验室：比较设计，再决定偏爱记在哪里。" width="100%"></a>
<p>本地规则 · 明确授权范围<br><a href="https://andyzhang666666.github.io/tasteroom/">体验</a> · <a href="https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/tasteroom">源码与设计</a></p>
</td>
<td width="50%" valign="top">
<p><strong>Bundle Lab</strong><br>新增贡献和既有顾客让利分开算。</p>
<a href="https://andyzhang666666.github.io/bundle-lab/"><img src="docs/assets/bundle-preview.jpg" alt="Bundle Lab：新增贡献和既有顾客让利分开算。" width="100%"></a>
<p>合成订单 · 条件推演<br><a href="https://andyzhang666666.github.io/bundle-lab/">体验</a> · <a href="https://github.com/AndyZhang666666/bundle-lab">源码与设计</a></p>
</td>
</tr>
</table>

[Agent 静态图](docs/assets/agent-preview.jpg)。动图是程序记录的逐步回放，停留时长用于演示，不表示执行耗时。

### Agent 与评测：把完成条件做进产品

[Agent 执行评测台](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/agent-bench)、[可信 RAG 实验台](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/main/rag-lab)和 [Eval Lab](https://github.com/AndyZhang666666/llm-output-eval)分别检查执行、依据和输出质量。

Agent 台用十个虚构工单案例检查权限、失败恢复和重复写入。RAG 台让同一问题随日期、资料版本和可访问范围改变，答案与来源一起复核。Eval 保留裁判原分，让人的不同判断也能留下来。

[体验 RAG](https://andyzhang666666.github.io/rag-lab/) · [查看 RAG 的检索与版本机制](https://github.com/AndyZhang666666/AndyZhang666666.github.io/blob/main/rag-lab/engine.mjs) · [公告事实与遗漏复核](https://github.com/AndyZhang666666/filing-eval)

### 生活产品：保留人的决定权

**[偏爱实验室 · TasteRoom](https://andyzhang666666.github.io/tasteroom/)** 把审美探索做成比较、归因和授权。瑞士现代主义与解构主义是可操作的设计方向；喜欢一张海报，不会被直接记成所有场景下的偏好。

**[随便局](https://andyzhang666666.github.io/suibianju/)** 处理朋友聚餐里的“随便”。没有共同选项时，先预演自愿调整，再由成员确认条件和同一版方案。**[有据 · Grounded Choice](https://andyzhang666666.github.io/grounded-choice/)** 则保留经验的共识、分歧和适用条件，让用户自己比较与选择。

### 增长与商业化：让账本回答问题

| 工具 | 我想回答的问题 | 实现 |
| --- | --- | --- |
| [Bundle Lab](https://github.com/AndyZhang666666/bundle-lab) · [体验](https://andyzhang666666.github.io/bundle-lab/) | 经常一起买，是否就值得打折？ | 共购发现、两类人群账本、平衡点与验证计划。 |
| [Growth Experiment Lab](https://github.com/AndyZhang666666/growth-experiment-lab) · [体验](https://andyzhang666666.github.io/growth-experiment-lab/) | 显著之后，是否值得全量？ | 实验设计、反复查看风险、护栏与人工发布判断。 |
| [Pricing Model Sim](https://github.com/AndyZhang666666/pricing-model-sim) · [体验](https://andyzhang666666.github.io/pricing-model-sim/) | 同一批用户，哪种付费机制更合适？ | 人群守恒、逐月收入、假设扫描与折现回本。 |

## 工作中的产品实践

在山海星辰负责创作 Agent 与 Skill 资产：上线 38 个 Skill，工具月均调用约 6,000 次，单剧创作耗时缩短约 30%。在百度实习时参与 AI 功能从 0 到 1，上线两周日活破万；在美团 Keeta 的增长实习中，分层补贴实验使新客获客成本降低 27%，新客月留存提升 8%。也有理想汽车智能座舱和 Revolut 订阅产品的实习经历。

[具体职责与结果口径](https://andyzhang666666.github.io/#work) · [产品简历](https://andyzhang666666.github.io/assets/resume.pdf)

上面是工作经历中的业务结果；这里的公开代码是独立作品。演示资料、历史模型输出和条件模拟在项目中分别标明，不包含公司内部代码或业务数据。Agent / RAG 的公开站点分别为程序记录回放和浏览器检索，真实模型接入需自行配置。

## 还在做什么

[AI 产品拆解](https://github.com/AndyZhang666666/ai-product-teardowns)用同一套问题比较产品的能力边界、失败处理与付费点；[通勤比较器](https://github.com/AndyZhang666666/commute-compare)和[扑克决策工具](PROJECTS.md#日常决策与建模)用来练习风险、假设和不确定性的表达。[Creative Eval](https://github.com/AndyZhang666666/creative-eval)保留了 Eval 第一版的校准过程与历史结果。

UCL 硕士 · Bristol 电子电气工程本科。研究过订单流日内量化模型，也做过面向运动场景的可穿戴姿态监测与手机交互。

[联系我](https://andyzhang666666.github.io/#contact) · [English](README.en.md) · [按方向浏览全部项目](PROJECTS.md)
