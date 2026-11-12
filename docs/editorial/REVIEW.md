# GitHub 主页候选版交付记录

2026-11-12。本版为**待审阅候选，尚未合并到个人主页主分支**。本轮重做中英文 README 的展示结构与素材，官网、Demo 功能、置顶顺序和既有履历保持现状。

## 固定预览与原版

- 候选中文版：[README.md](https://github.com/AndyZhang666666/AndyZhang666666/blob/d531789aac082f007ca5fcfe0ec2c218779a9c2a/README.md)
- 候选英文版：[README.en.md](https://github.com/AndyZhang666666/AndyZhang666666/blob/d531789aac082f007ca5fcfe0ec2c218779a9c2a/README.en.md)
- 原版：[中文](https://github.com/AndyZhang666666/AndyZhang666666/blob/ae171a4355b9c21f463f15df9d793c9c4b937d64/README.md) · [英文](https://github.com/AndyZhang666666/AndyZhang666666/blob/ae171a4355b9c21f463f15df9d793c9c4b937d64/README.en.md)

主分支基线：`ae171a4355b9c21f463f15df9d793c9c4b937d64`。本次已视觉核对的候选提交：`d531789aac082f007ca5fcfe0ec2c218779a9c2a`。文档中的固定链接用于复核这个版本，不随后续分支移动。

## 改了什么

采用瑞士编辑式排版与一处轻微错位图形：姓名与定位 → Eval 主作品 → TasteRoom、Bundle、RAG 三个精选 → 三条真实交付 → 职责与折叠经历 → 完整目录与联系。

封面和作品共享明暗配色、字体层级与版心。作品素材来自本次重新操作的截图，以外部版式和取景突出一个具体任务，不修改原始 UI 数值。封面、Eval、RAG 另有窄屏素材；核心判断与入口始终由 GitHub 原生文字承担，不让图片成为唯一的信息来源。

四个作品各保留“体验 / 设计与实现”两个主入口。承接页集中提供问题、设计取舍、完整截图、固定源码和 11/11 任务记录：[Eval](projects/eval.md) · [TasteRoom](projects/taste.md) · [Bundle](projects/bundle.md) · [RAG](projects/rag.md)。

Eval 的 [7 秒任务回放](replay/eval-task-7s.gif) 由三张真实状态截图编码，手动打开；不是连续录像，也不是延迟测量。人工审阅、构造资料、条件毛利和本机规则核查的边界均保留，没有新增未经证实的业绩或模型效果。

## 真实修改记录

| 提交 | 内容 |
|---|---|
| [`1074a29`](https://github.com/AndyZhang666666/AndyZhang666666/commit/1074a29) | 制作原创封面、四组产品素材、原始截图与短回放，并记录来源。 |
| [`145d5c5`](https://github.com/AndyZhang666666/AndyZhang666666/commit/145d5c5) | 重排中英文主页，接入作品承接页、目录与审阅入口。 |
| [`d531789`](https://github.com/AndyZhang666666/AndyZhang666666/commit/d531789aac082f007ca5fcfe0ec2c218779a9c2a) | 根据 GitHub 原生预览微调截图取景与衔接。 |

## 实际核对范围

在同一候选提交的 GitHub 原生 README 页面，核对了 **12 个状态**：中文、英文 × 1280 / 768 / 390px 视口 × 浅色、深色。

- 60 个实际图片实例均选择对应主题和宽度的资源，具有替代说明；图片显示宽度未超过文档宽度，页面记录未发现横向溢出。
- 人工查看明暗、桌面、平板与手机截图，没有发现明显的意外截字、非等比拉伸、图像缺失或章节拼接错误。Eval、Taste、Bundle、RAG 的阅读顺序与文案一致。
- 手机中 Taste、Bundle 的部分 UI 细字仍需放大或进入设计页；不能声称所有图内小字都同样易读。主要判断、边界及体验入口由原生正文保留。
- 全页捕获中的固定文件导航、长空白尾部和初次缺尾按截图边界记录，不误判成产品 UI 缺失。中文浅色手机与英文深色手机均补查了页尾截图，确认职责、折叠经历、分类、联系与来源入口；两处证据缺口已关闭。
- 结构检查覆盖当时的 11 份 Markdown、91 个相对目标，未发现失效目标；七张原始截图与清单的尺寸、字节和 SHA-256 一致。16 份 SVG 可解析，嵌入 JPEG 与原始截图一致，没有引入脚本、事件或外部依赖。

[12 组显示记录](review/github-render-checks-final.json) · [结构检查](review/structure-check-final.json) · [来源与发布核对](review/source-ref-check.json)。

这些是展示、结构与来源核对，不代表重新完成所有 Demo 的功能验收，不是模型效果测试，也不是设计评分。GitHub 文件预览的 Code、提交信息和固定导航属于平台外壳，最终个人主页的外壳与此不同。

## 资源体积

| 资源 | 实际大小 |
|---|---:|
| 默认五张静态图，单个主题 | 545,573 B |
| 窄屏五张静态图，单个主题 | 544,882 B |
| 手动打开的三状态回放 | 371,590 B，7 秒 |

静态资源低于 700KB 目标，回放低于 1.5MB 目标。体积不等于加载速度，未以这些数字推导性能成绩。

## 前后对照

- [原版作品区](review/before-gallery-light.jpg)
- [候选封面与首段](review/cover-light.jpg)
- [候选 Eval 主作品](review/eval-light.jpg)
- [中文浅色手机页尾补图](review/zh-mobile-light-bottom.jpg)
- [英文深色手机页尾补图](review/en-mobile-dark-bottom.jpg)

图片为真实 GitHub 审阅页面的截图；全页或拼接捕获不是连续录像。它们说明可见内容和排版，不证明滚动流畅度或产品响应延迟。

## 保留与来源

原始 [中文完整目录](../../PROJECTS.md)、[英文完整目录](../../PROJECTS.en.md)、旧素材及修改历史保留；工作经历与研究背景完整放在折叠区。本轮不改官网、Demo 功能或原生六个置顶仓库。

[素材来源与事实边界](SOURCES.md) · [逐图与版本清单](source-manifest.json) · [第三方参考与许可](REFERENCES.md)。参考模板只提供编排原则，不把作者的人像、指标、代码或身份作为本人作品发布，不改变原项目许可。

本轮已安装并应用两份专用指导资源：[github-profile-readme](https://github.com/boffti/github-profile-readme/tree/dc83eadfcec56bc522e3a6fe60d8fa3ea5ebb1ca)，固定来源 `dc83eadfcec56bc522e3a6fe60d8fa3ea5ebb1ca`；[github-profile](https://github.com/jdevalk/skills/tree/106fc68014b6275300b8206ad94b8facc1549577/github-profile)，固定来源 `106fc68014b6275300b8206ad94b8facc1549577`。它们帮助整理内容与审阅，不替代实际 GitHub 视觉核对。

下一步是审阅候选观感；确认后再决定合并发布。
