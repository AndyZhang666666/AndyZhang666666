# 展示素材来源与事实边界

本轮素材于 **2026-11-12** 使用 CUA 在公开产品中重新操作并截取。演示输入为明确构造的资料，不使用雇主内部材料，不把手动输入写成模型生成，不把条件推演写成真实业务收益。此次仅更新 GitHub 展示素材，未修改四个产品代码。

原始 JPEG 保存在 [raw/](raw/)，均为完整浏览器视口截图。逐图尺寸、字节与 SHA-256，以及产品地址、源码版本和演示条件，见 [source-manifest.json](source-manifest.json)。源码版本来自同日远端引用核对，不是截图服务器的部署证明。

## 产品与版本

| 产品 | 体验 | 对照源码提交 |
|---|---|---|
| Eval Lab | [文稿工作区](https://andyzhang666666.github.io/llm-output-eval/workspace/) | [`af60f5b`](https://github.com/AndyZhang666666/llm-output-eval/tree/af60f5b096bfd4e09ef0e5c94d5f8a93f44a1b40) |
| TasteRoom | [偏爱实验室](https://andyzhang666666.github.io/tasteroom/) | [`174399e`](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/174399eef34fcdaae22926585dcf9066d1a283bb/tasteroom) |
| Bundle Lab | [收益推演](https://andyzhang666666.github.io/bundle-lab/simulate/) | [`062b656`](https://github.com/AndyZhang666666/bundle-lab/tree/062b6563a9e587c27040f6fc596184f58d0407b3) |
| 可信 RAG | [资料与草稿](https://andyzhang666666.github.io/rag-lab/) | [`174399e`](https://github.com/AndyZhang666666/AndyZhang666666.github.io/tree/174399eef34fcdaae22926585dcf9066d1a283bb/rag-lab) |

## 四个真实操作场景

### Eval：人工审阅、修改与逐字对照

导入一份 50 字构造短篇作为 V1，选择对白相关原文并填写人工观察，然后建立 V2 修改稿，查看两个版本的逐字增删。

- [eval-review.jpg](raw/eval-review.jpg)：V1 原文、引用及人工对白意见。界面明确显示“尚无模型评测”“这里没有模型分数”。
- [eval-revision.jpg](raw/eval-revision.jpg)：修改稿状态。
- [eval-diff.jpg](raw/eval-diff.jpg)：原稿与修改稿的逐字对照。

本次不调用模型，也不展示虚构模型分数。人工意见与模型原分是不同记录，不能将这份人工审阅截图解释为模型效果证明。

### TasteRoom：同文同图，不同授权范围

[taste-scene.jpg](raw/taste-scene.jpg) 两侧使用相同默认文案；本例未上传主图，两侧的主图输入均为空。个人场景有一条字体授权，构图使用默认瑞士现代主义；工作场景有一条明确授权的解构主义规则。两个场景均显示一条场景授权、零条全局继承。

打开对照是只读操作：查看、临时试用与写入长期偏好分别处理，不因浏览对照自动保存偏好。

### Bundle：新增贡献与既有让利

[bundle-ledger.jpg](raw/bundle-ledger.jpg) 切换到内置合成订单，选择可乐与鸡腿饭。条件为折扣 **12%**、中档新增采纳率 **12%**、既有顾客领折扣 **100%**。界面按每 100 个覆盖订单归一化，不是观测到的订单数。

- 新增毛利贡献：**¥46.11**。
- 既有顾客让利损失：**¥95.61**。
- 增量毛利：**¥−49.51**。

三个数字由界面分别从底层计算结果四舍五入，因此展示分项直接相减可能相差一分钱。素材保留原界面数值，不重算或“修正”总额。毛利不含履约、库存与运营等成本；本场景是条件推演，不是净利润或已经验证的经营结果。

### RAG：数字线索与资料适用性

粘贴构造的显示器借用资料：原文写最长 **14 天**，人工编辑的答复草稿写 **12 天**。这份草稿来自操作人，不是模型结论。

- [rag-numeric.jpg](raw/rag-numeric.jpg)：数字线索核查。找不到“12 天”的相应原文时，界面提示核对；文字匹配不代表语义正确。
- [rag-condition.jpg](raw/rag-condition.jpg)：将业务日期由 **2026-10-28** 改为 **2026-11-12**，已选的旧依据提示需要重查；未重新确认适用性前禁止导出。

本次仅使用浏览器本机检索、规则核查和人工草稿，未调用模型。资料条件变化后的提示不等于系统已自动完成适用性判断。

## 原图与展示图的关系

原始 JPEG 不修改。最终展示图允许增加产品外部的标题、留白、标签和版式，并使用 SVG 嵌套 `viewBox` 聚焦原界面的指定区域。不会重绘 UI、修改数字或替换原始状态。

展示窗口及素材校验值记录在清单中。展示图只使用此处保留的七张完整视口截图。

## Eval 短回放

回放制作约束：使用 `eval-review.jpg`、`eval-revision.jpg`、`eval-diff.jpg` 三张真实操作截图编码为 **7 秒、三状态任务回放**。README 默认展示静态图，由文字链接手动打开回放。

它是截图组成的任务序列，**不是连续录屏，不测量执行耗时或系统延迟**。成品共 3 帧，实际总时长 7,000 毫秒，文件 371,590 字节；SHA-256 与各帧时长见清单。

## 第三方参考

参考模板只用于理解网格、基线、强调色与编辑式编排。来源、固定提交和许可边界见 [REFERENCES.md](REFERENCES.md)。参考作者的个人资料、头像、指标与源码未作为本人作品发布，也未改变现有项目许可。
