# 主页审阅 · 2026-11-23

[中文候选](https://github.com/AndyZhang666666/AndyZhang666666/blob/547bfcf87c8cf930d86749ddd7a1e8e3f5a7b884/README.md) · [English candidate](https://github.com/AndyZhang666666/AndyZhang666666/blob/547bfcf87c8cf930d86749ddd7a1e8e3f5a7b884/README.en.md) · [改版前](https://github.com/AndyZhang666666/AndyZhang666666/blob/c8760f26af49716b02feb6600a38cc73f0ac2dbb/README.md)

| GitHub 实际取景 | 改版前 | 候选 |
| --- | --- | --- |
| 桌面，1280 × 900 | [原版](before-zh-1280-light.jpg) | [新版](candidate-zh-1280-light.jpg) |
| 手机，390 × 844 | [原版](before-zh-390-light.jpg) | [新版](candidate-zh-390-light.jpg) · [英文深色](candidate-en-390-dark.jpg) |

截图均将 README 封面顶部对齐同一位置，保留 GitHub 文件预览工具栏。候选页核对了两种语言、两个宽度及明暗两种主题。每种组合的五幅图片均已解码，三个任务入口在封面下方可见，文档宽度与视口宽度一致。[逐项检查](native-render.json)

## 三个可以复现的动作

| 入口 | 公开示例的操作与结果 |
| --- | --- |
| Eval | 从 e06 的结构评分 2/5 点“定位到原文”，被标出的句子停在“他看清了那人胸牌上的”。查看历史回放无需模型调用。 |
| Growth | 新窗口直接进入结果解读器。合成样例的 p = 0.0492；区间下界仍低于预设业务门槛，护栏尚待核对，页面显示“暂不全量”。 |
| Bundle | 合成订单，中档采纳率固定在 12%。折扣 6% 时每百笔覆盖订单的条件增量毛利为 +¥13.44，折扣 8% 时为 −¥7.54。 |

[重复运行的浏览器检查](../../../scripts/check-public-tasks.mjs)从新浏览器会话访问公开入口，拦截写入请求。测试环境安装 Playwright 及 Chromium 后可运行 `node scripts/check-public-tasks.mjs`。使用 Chrome 时设 `BROWSER_CHANNEL=chrome`。链接检查采用 Lychee 0.24.2，对双语 README、双语索引、素材说明及四份设计页检查了 226 个链接引用，95 个不同目标，错误 0。[链接检查输出](lychee-final.json)

官网的三方向简历选择器已经公开。三份入口均返回可读的 PDF 文件头。主页另有 Keeta 跨语言搜索案例入口，定价算例和检索实践分别展示。两版履历材料中尚缺原始记录支持的统计量与日期，未写入新版主页。

**English.** The draft reconciles the published profile with the editorial preview. Three public task links precede the Eval case. Historical output, simulated experiments and conditional margins are labelled at the point of use. The desktop and mobile comparisons above use GitHub’s native file view. Product code and deployment are outside this change.
