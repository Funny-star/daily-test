import pygame
import math
import random
import sys

# 初始化pygame
pygame.init()

# 设置窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("粒子效果跳动的心")

# 颜色
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 105, 180)
COLORS = [(255, 0, 0), (255, 20, 147), (255, 105, 180), (255, 192, 203)]

# 粒子类


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = random.choice(COLORS)
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)
        self.distance = random.uniform(0, 10)
        self.original_x = x
        self.original_y = y

    def update(self, beat):
        # 粒子向外扩散
        self.distance += self.speed * 0.1
        # 心跳效果
        pulse = math.sin(beat) * 5
        self.x = self.original_x + \
            math.cos(self.angle) * (self.distance + pulse)
        self.y = self.original_y + \
            math.sin(self.angle) * (self.distance + pulse)

        # 如果粒子太远，重置它
        if self.distance > 50:
            self.distance = 0
            self.angle = random.uniform(0, 2 * math.pi)
            self.speed = random.uniform(0.5, 2)
            self.color = random.choice(COLORS)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (int(self.x), int(self.y)), self.size)

# 创建心形函数


def heart_x(t, size=10):
    return size * 16 * (math.sin(t) ** 3)


def heart_y(t, size=10):
    return size * (-13 * math.cos(t) + 5 * math.cos(2*t) + 2 * math.cos(3*t) + math.cos(4*t))


# 创建粒子
particles = []
for i in range(500):
    t = random.uniform(0, 2 * math.pi)
    x = width // 2 + heart_x(t, 10)
    y = height // 2 + heart_y(t, 10)
    particles.append(Particle(x, y))

# 主循环
clock = pygame.time.Clock()
beat = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清屏
    screen.fill(BLACK)

    # 更新心跳
    beat += 0.1

    # 更新和绘制粒子
    for particle in particles:
        particle.update(beat)
        particle.draw(screen)

    # 绘制心形轮廓
    points = []
    for t in range(0, 628, 1):  # 0 到 2π
        t = t / 100
        x = width // 2 + heart_x(t, 10)
        y = height // 2 + heart_y(t, 10)
        points.append((x, y))

    if len(points) > 1:
        pygame.draw.lines(screen, RED, False, points, 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
