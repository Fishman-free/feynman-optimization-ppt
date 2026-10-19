# 费曼学习法是一阶优化算法 · 网页 PPT 设计文档

- 日期：2026-10-19
- 状态：用户已批准方向与设计方案（对话确认「好的 你开工吧」）
- 交付：`ppt/index.html`（单文件瑞士风网页 PPT，含演讲者模式）+ `演讲稿.md`（12 段逐页讲稿）

## 1. 核心论点

费曼学习法四步是一阶优化循环，逐行映射：

| 费曼学习法（原书） | 一阶优化算法 |
|---|---|
| 确立目标（SMART 原则） | 定义损失函数 |
| 以教代学、尝试输出 | 前向传播，产生预测 |
| 卡壳、回顾、纠错 | 回传梯度信号 |
| 简化、复述到流畅 | 收敛判据 |

收尾推论：AI 时代写 prompt、给 AI 讲清需求 = 费曼学习法的变形，教机器也是教；人和 LLM 都在做梯度下降，但人的损失函数是社会性定义的（别人听懂没有）。

## 2. 页面计划（12 页 ≈ 13 分钟，15 分钟预算的 87%）

| 页 | slide-id | 版式 | 主题 | 内容 | 时长(min) |
|---|---|---|---|---|---:|
| 1 | cover | SWISS-COVER-ASCII | hero dark | 封面：费曼学习法是一阶优化算法 | 0.5 |
| 2 | hook | S09 | hero light | 钩子：读了三遍为什么还是讲不出来（输入不收敛） | 1 |
| 3 | feynman-loop | S14 | light | 原书框架：四步循环 + 输出倒逼输入 | 1 |
| 4 | mapping | S08 | dark | 核心论点页：四步 × 优化四要素逐行映射 | 1.5 |
| 5 | loss-function | S03 | light | SMART 目标 = 定义可度量损失函数；L = 复述流畅度误差 | 1.5 |
| 6 | gradient-signal | S12 | dark | 卡壳不是失败，是梯度信号（误差反传） | 1 |
| 7 | data-evidence | S06 | light | 数据分析：Karpicke & Roediger 2008（Science）检索练习 ~56% vs 重复阅读 ~36%；开环/闭环收敛仿真 | 1.5 |
| 8 | failure-modes | S05 | light | 三种不收敛：开环 / 零步长（只读不写）/ 局部最优（死记硬背=过拟合） | 1.5 |
| 9 | forgetting-curve | S02 | dark | 遗忘曲线 R = e^(−t/S)；间隔重复 = 随机重启/学习率调度 | 1.5 |
| 10 | simplification | S16 | light | 简化 = 正则化：术语→白话→类比；「讲到小孩懂」= 分布外泛化测试 | 1 |
| 11 | ai-era | S18 | light | 推论：AI 时代费曼学习法升值；教机器也是教 | 1.5 |
| 12 | closing | S10 | dark | 金句「学习的收敛判据，是别人听懂了」+ 行动清单 | 1 |

合计 14 min 上限内压到 13 min（validator 按 90% 预算校验时 target-minutes 15）。

主题节奏：dark/light 交替，无三连同主题；12 页用 12 个不同登记版式。

## 3. 数据与建模

- 真实实验：Karpicke & Roediger (2008, Science)——重复阅读组一周后留存约 36%，检索测试组约 56%。用于替代流传的无出处「学习金字塔」数字。
- 收敛仿真（Python 本地跑）：开环（只输入）理解度随机漂移不收敛；闭环（输出-纠错）按迭代收敛。产出具体数字写进 KPI 组件。
- 遗忘曲线：R = e^(−t/S)，输出提高记忆强度 S；间隔重复 = 衰减到阈值前的随机重启。

## 4. 视觉规范

- 风格 B 瑞士国际主义，`assets/template-swiss.html` 为种子
- 主题色：🔵 克莱因蓝 IKB（--accent:#002FA7），单一锚点色，不混搭
- 正文页全部使用登记版式 S01-S22 + SWISS-COVER-ASCII，每页写 data-layout
- 中文大标题按字号分档表限高（min(Xvw, Yvh)）；小字下限 14px，正文下限 18px
- 图表用模板内置 CSS 组件（KPI 塔 / 条形图），不依赖外部图片

## 5. 演讲备注与讲稿

- 每页唯一稳定 data-slide-id（上表第 2 列），SPEAKER_NOTES 按 id 存储，字段：purpose / talk / transition / minutes / section
- 备注写提词卡式 3-5 条要点；另交付 `演讲稿.md` 逐页完整讲稿（每页 150-250 字）

## 6. 验收

- `node scripts/validate-swiss-deck.mjs ppt/index.html` 通过
- `node scripts/validate-presenter-mode.mjs ppt/index.html --target-minutes 15` 通过
- 对照 `references/checklist.md` 瑞士风 24 条自检
