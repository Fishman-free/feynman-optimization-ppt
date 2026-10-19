# -*- coding: utf-8 -*-
"""
费曼学习法 × 一阶优化：开环 vs 闭环学习收敛仿真
模型：
  gap_t = |理解度_hat - 真实掌握度|，初始 gap_0 = 1.0（完全没掌握）
  开环（只输入不输出）：误差不可观测，gap 做带噪声的随机游走，系统不收敛
  闭环（输出-卡壳-纠错）：每次迭代观测并消除比例为 delta 的误差，gap 几何收敛
"""
import json
import random

random.seed(42)

N_ITER = 12
DELTA = 0.35          # 每次输出-纠错消除 35% 的残余误差
NOISE = 0.08          # 开环漂移噪声幅度
TRIALS = 2000


def closed_loop():
    g, curve = 1.0, [1.0]
    for _ in range(N_ITER):
        g *= (1 - DELTA)
        curve.append(g)
    return curve


def open_loop():
    g, curve = 1.0, [1.0]
    for _ in range(N_ITER):
        # 没有反馈：自以为在进步（主观理解度上升），真实误差原地漂移
        g = min(1.2, max(0.55, g + random.uniform(-NOISE, NOISE)))
        curve.append(g)
    return curve


# 多次试验取均值
open_runs = [open_loop() for _ in range(TRIALS)]
open_mean = [sum(r[i] for r in open_runs) / TRIALS for i in range(N_ITER + 1)]
closed_mean = closed_loop()

print("迭代次数 | 开环误差(均值) | 闭环误差")
for i in range(0, N_ITER + 1, 2):
    print(f"  {i:2d}    |    {open_mean[i]:.3f}      |  {closed_mean[i]:.3f}")

final_open = sum(r[-1] for r in open_runs) / TRIALS
below_10 = sum(1 for r in open_runs if r[-1] < 0.10) / TRIALS
print(f"\n12 次迭代后：闭环误差 {closed_mean[-1]:.3f}（收敛）；开环均值 {final_open:.3f}，仅 {below_10:.1%} 的试验误差低于 0.10（靠运气）")

# 遗忘曲线 R = e^(-t/S)：重复阅读 vs 输出后的记忆强度
import math
for S, label in [(2.0, "重复阅读 S=2"), (6.0, "输出后 S=6")]:
    r7 = math.exp(-7 / S)
    print(f"{label}：7 天后留存 {r7:.1%}")

result = {
    "open_loop_final_mean": round(final_open, 3),
    "closed_loop_final": round(closed_mean[-1], 3),
    "closed_below_10pct_at_iter": next(i for i, g in enumerate(closed_mean) if g < 0.10),
    "retention_7d_reading": round(math.exp(-7 / 2.0), 3),
    "retention_7d_output": round(math.exp(-7 / 6.0), 3),
}
with open("scripts/sim_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("\n已写入 scripts/sim_result.json")
