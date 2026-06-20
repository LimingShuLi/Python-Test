import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.interpolate import make_interp_spline

# ==================== 字体设置 ====================
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# ==================== 数据 =====================
f1 = np.array([0.7, 0.9, 1.1, 1.3, 1.477, 1.7, 1.9, 2.3, 3.0])
f2 = np.array([0.5, 0.8, 1.1, 1.3, 1.523, 1.8, 2.1, 2.5, 3.0])
U0_100 = np.array([0.167, 0.257, 0.409, 0.622, 0.804, 0.667, 0.512, 0.332, 0.205])
U0_400 = np.array([0.418, 0.769, 1.277, 1.639, 1.810, 1.629, 1.318, 1.007, 0.770])

# ==================== 平滑插值 ====================
# 生成更密集的插值点（500个点）
f1_smooth = np.linspace(f1.min(), f1.max(), 500)

# 使用 cubic spline 插值，k=3 表示三次样条
spl_100 = make_interp_spline(f1, U0_100, k=3)
U0_100_smooth = spl_100(f1_smooth)

spl_400 = make_interp_spline(f1, U0_400, k=3)
U0_400_smooth = spl_400(f1_smooth)

# 生成更密集的插值点（500个点）
f2_smooth = np.linspace(f2.min(), f2.max(), 500)

# 使用 cubic spline 插值，k=3 表示三次样条
spl_100 = make_interp_spline(f2, U0_100, k=3)
U20_100_smooth = spl_100(f2_smooth)

spl_400 = make_interp_spline(f2, U0_400, k=3)
U20_400_smooth = spl_400(f2_smooth)

# ==================== 图1: R = 100 Ω ====================
fig1, ax1 = plt.subplots(figsize=(8, 5))

# 绘制平滑曲线
ax1.plot(f1_smooth, U0_100_smooth, '-', color='#1f77b4', linewidth=2, label=r'$R = 100\,\Omega$')
# 叠加原始数据点（zorder=5 确保点在曲线上方）
ax1.plot(f1, U0_100, 'o', color='#1f77b4', markersize=8, zorder=5)

ax1.set_xlabel(r'频率 $f$ (kHz)', fontsize=12)
ax1.set_ylabel(r'电阻电压 $U_0$ (V)', fontsize=12)
ax1.set_title(r'幅频特性曲线 ($R = 100\,\Omega$) — 平滑插值', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(fontsize=11)

# 标记峰值点
peak_idx = np.argmax(U0_100)
ax1.plot(f1[peak_idx], U0_100[peak_idx], 'ro', markersize=10, zorder=6)
ax1.annotate(
    f'峰值: ({f1[peak_idx]} kHz, {U0_100[peak_idx]} V)',
    xy=(f1[peak_idx], U0_100[peak_idx]),
    xytext=(f1[peak_idx] + 0.3, U0_100[peak_idx] ),
    fontsize=10,
    arrowprops=dict(arrowstyle='->', color='red')
)

plt.tight_layout()
fig1.savefig('U0_f_R100_smooth.png', dpi=300)
plt.show()

# ==================== 图2: R = 400 Ω ====================
fig2, ax2 = plt.subplots(figsize=(8, 5))

# 绘制平滑曲线
ax2.plot(f2_smooth, U20_400_smooth, '-', color='#ff7f0e', linewidth=2, label=r'$R = 400\,\Omega$')
# 叠加原始数据点
ax2.plot(f2, U0_400, 's', color='#ff7f0e', markersize=8, zorder=5)

ax2.set_xlabel(r'频率 $f$ (kHz)', fontsize=12)
ax2.set_ylabel(r'电阻电压 $U_0$ (V)', fontsize=12)
ax2.set_title(r'幅频特性曲线 ($R = 400\,\Omega$) — 平滑插值', fontsize=14)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(fontsize=11)

# 标记峰值点
peak_idx = np.argmax(U0_400)
ax2.plot(f2[peak_idx], U0_400[peak_idx], 'ro', markersize=10, zorder=6)
ax2.annotate(
    f'峰值: ({f2[peak_idx]} kHz, {U0_400[peak_idx]} V)',
    xy=(f2[peak_idx], U0_400[peak_idx]),
    xytext=(f2[peak_idx] + 0.3, U0_400[peak_idx] + 0.03),
    fontsize=10,
    arrowprops=dict(arrowstyle='->', color='red')
)

plt.tight_layout()
fig2.savefig('U0_f_R400_smooth.png', dpi=300)
plt.show()