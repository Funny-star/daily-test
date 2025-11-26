import pygame as pg


# 初始化pygame
pg.init()

# 创建窗口
window = pg.display.set_mode((800, 600))

# 设计标题
pg.display.set_caption('Hello Pygame')

# 设置颜色
window.fill('black')

'''
在此位置放置绘图文件
'''
# pg.draw.aaline(window, color=('red'), start_pos=(
#     20, 30), end_pos=(100, 200), blend=1)
# point = [(50, 50), (50, 100), (200, 100)]
# pg.draw.lines(window, points=point,color=('red'), closed=True)

x = 400
y = 300
# 绘制圆
pg.draw.circle(window, color=('red'), center=(x, y), radius=10, width=2)


# 绘制矩形
# pg.draw.rect(window, color=('red'), rect=(30, 30, 100, 30),
#              width=2, border_radius=15)  # 当width无申明时为默认填满矩形

# pg.draw.rect(window, color=('red'), rect=(30, 30, 100, 30),
#              width=2, border_top_left_radius=15, border_bottom_left_radius=17)
pg.display.update
while True:

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        x -= 4
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        x += 4
    if keys[pg.K_UP] or keys[pg.K_w]:
        y -= 4
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        y += 4
    pg.display.update()


# 跟新窗口


# 让窗口暂停
# pg.time.wait(1000)


# 清理退出pygame
pg.quit()
