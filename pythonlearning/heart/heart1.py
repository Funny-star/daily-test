import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

# 设置中文字体（可选，用于显示中文标签）
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(8, 7))
fig.patch.set_facecolor('black')  # 设置背景为黑色
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # 隐藏坐标轴

# 爱心参数方程


def heart_x(t, size=1):
    return size * 16 * np.sin(t) ** 3


def heart_y(t, size=1):
    return size * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))


# 初始化爱心
t = np.linspace(0, 2*np.pi, 1000)
size = 0.1
line, = ax.plot(heart_x(t, size), heart_y(t, size), color='red', linewidth=3)

# 添加文本
text = ax.text(0, -1.5, '❤️ 跳动的心 ❤️', fontsize=20, color='white',
               ha='center', va='center')

# 动画更新函数


def update(frame):
    # 使用正弦函数创建跳动效果
    pulse = 0.1 * np.sin(frame * 0.2) + 1
    current_size = size * pulse

    # 更新爱心大小
    line.set_data(heart_x(t, current_size), heart_y(t, current_size))

    # 改变颜色（可选）
    r = (np.sin(frame * 0.1) + 1) / 2
    g = 0
    b = (np.cos(frame * 0.1) + 1) / 2
    line.set_color((r, g, b))

    # 文本跳动效果
    text.set_fontsize(15 + 5 * np.sin(frame * 0.2))

    return line, text


# 创建动画
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
