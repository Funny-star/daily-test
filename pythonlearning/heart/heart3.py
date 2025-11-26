import math
import pygame as pg

# 变量
x = None
y = None


def heart_x(t, size=10):
    return size * 16 * (math.sin(t) ** 3)


def heart_y(t, size=10):
    return size * (-13 * math.cos(t) + 5 * math.cos(2*t) + 2 * math.cos(3*t) + math.cos(4*t))


particles = []
for t in range(0, 628, 1):  # 0 到 2π
    t = t / 100
    x = 300 // 2 + heart_x(t, 10)
    y = 300 // 2 + heart_y(t, 10)
    particles.append(Particle(x, y))

    pg.init()
    screen = pg.display.set_mode(300, 300)
