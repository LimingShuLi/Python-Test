import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，防止图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 1. 一阶RC低通电路数据
lpf_f = np.array([0.5, 1, 2, 3, 4.823, 6, 10, 15, 30]) # kHz
lpf_H = np.array([0.972, 0.954, 0.893, 0.814, 0.673, 0.594, 0.412, 0.291, 0.153])
lpf_phase = np.array([-6.3, -12.2, -23.3, -32.0, -43.5, -48.6, -58.3, -61.0, -54.5]) # °

# 2. 一阶RC高通电路数据
hpf_f = np.array([1, 3, 6, 10, 15.915, 20, 25, 30, 50]) # kHz
hpf_H = np.array([0.0639, 0.187, 0.353, 0.527, 0.697, 0.771, 0.831, 0.872, 0.944])
hpf_phase = np.array([121.0, 99.4, 77.9, 62.6, 47.0, 40.3, 35.1, 28.1, 17.6]) # °

# 3. RC选频网络(文氏电桥)数据
bp_f = np.array([0.05, 0.1, 0.2, 0.3, 0.362, 0.4, 0.6, 0.8, 1.2]) # kHz
bp_H = np.array([0.131, 0.222, 0.304, 0.328, 0.331, 0.331, 0.316, 0.293, 0.247])
bp_phase = np.array([67.0, 46.1, 22.5, 8.65, 0, -2.74, -17.5, -25.9, -40.3]) # °

# 绘图
fig = plt.figure(figsize=(15, 12))

# # --- 低通滤波器 ---
plt.subplot(3, 2, 1)
plt.semilogx(lpf_f, lpf_H, 'bo-', linewidth=2, markersize=6)
plt.title('RC低通滤波器 - 幅频特性')
plt.xlabel('频率 f (kHz)')
plt.ylabel('传输系数 H')
plt.grid(True, which="both", ls="--")
plt.axvline(x=4.823, color='r', linestyle=':', label=f'fc = 4.823 kHz')
plt.legend()

plt.subplot(3, 2, 2)
plt.semilogx(lpf_f, lpf_phase, 'ro-', linewidth=2, markersize=6)
plt.title('RC低通滤波器 - 相频特性')
plt.xlabel('频率 f (kHz)')
plt.ylabel('相位差 Φ (°)')
plt.grid(True, which="both", ls="--")
plt.axvline(x=4.823, color='r', linestyle=':', label=f'fc = 4.823 kHz')
plt.axhline(y=-45, color='g', linestyle=':', label='-45°')
plt.legend()

# --- 高通滤波器 ---
plt.subplot(3, 2, 3)
plt.semilogx(hpf_f, hpf_H, 'go-', linewidth=2, markersize=6)
plt.title('RC高通滤波器 - 幅频特性')
plt.xlabel('频率 f (kHz)')
plt.ylabel('传输系数 H')
plt.grid(True, which="both", ls="--")
plt.axvline(x=15.915, color='r', linestyle=':', label=f'fc = 15.915 kHz')
plt.legend()

plt.subplot(3, 2, 4)
plt.semilogx(hpf_f, hpf_phase, 'mo-', linewidth=2, markersize=6)
plt.title('RC高通滤波器 - 相频特性')
plt.xlabel('频率 f (kHz)')
plt.ylabel('相位差 Φ (°)')
plt.grid(True, which="both", ls="--")
plt.axvline(x=15.915, color='r', linestyle=':', label=f'fc = 15.915 kHz')
plt.axhline(y=45, color='g', linestyle=':', label='+45°')
plt.legend()

# --- 文氏电桥选频网络 ---
plt.subplot(3, 2, 3)
plt.semilogx(bp_f, bp_H, 'co-', linewidth=2, markersize=6)
plt.title('RC选频网络(文氏电桥) - 幅频特性')
plt.xlabel('频率 f (kHz)')
plt.ylabel('传输系数 H')
plt.grid(True, which="both", ls="--")
plt.axvline(x=0.362, color='r', linestyle=':', label=f'f0 = 0.362 kHz')
plt.legend()

plt.subplot(3, 2, 4)
plt.semilogx(bp_f, bp_phase, 'yo-', linewidth=2, markersize=6)
plt.title('RC选频网络(文氏电桥) - 相频特性')
plt.xlabel('频率 f (kHz)')
plt.ylabel('相位差 Φ (°)')
plt.grid(True, which="both", ls="--")
plt.axvline(x=0.362, color='r', linestyle=':', label=f'f0 = 0.362 kHz')
plt.axhline(y=0, color='g', linestyle=':', label='0°')
plt.legend()

plt.tight_layout()
plt.show()