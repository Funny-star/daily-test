import pygame as pg
import random as rd
# import time

# 常量
WIDTH = 1200
HEIGHT = 900


# 变量
position = [WIDTH//2, HEIGHT//2]
game_state = 'playing'
speed = 4
running = True
# 方向
up = [0, -speed]
down = [0, speed]
left = [-speed, 0]
right = [speed, 0]
direction = right
# 蛇相关变量
body_list = []
length_of_snake = 10
# 食物相关变量
number_of_food = 0
food_pos = [0, 0]


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill('black')


pg.display.update()


class snake():
    def __init__(self):
        pass

    # 四个方向的头部生成
    def draw_snake_head(self):
        global head
        x, y = position[0], position[1]
        if direction == left:
            head = pg.draw.rect(screen, color=('snow'), rect=(x, y, 15, 15),
                                width=10, border_top_left_radius=15, border_bottom_left_radius=15)
            pg.draw.circle(screen, color='black', center=(x+5, y+5), radius=2)
            pg.draw.circle(screen, color='black', center=(x+5, y+10), radius=2)
        if direction == right:
            head = pg.draw.rect(screen, color=('snow'), rect=(x, y, 15, 15),
                                width=10, border_top_right_radius=15, border_bottom_right_radius=15)
            pg.draw.circle(screen, color='black', center=(x+10, y+5), radius=2)
            pg.draw.circle(screen, color='black',
                           center=(x+10, y+10), radius=2)
        if direction == up:
            head = pg.draw.rect(screen, color=('snow'), rect=(x, y, 15, 15),
                                width=10, border_top_left_radius=15, border_top_right_radius=15)
            pg.draw.circle(screen, color='black', center=(x+5, y+5), radius=2)
            pg.draw.circle(screen, color='black', center=(x+10, y+5), radius=2)
        if direction == down:
            head = pg.draw.rect(screen, color=('snow'), rect=(x, y, 15, 15),
                                width=10, border_bottom_right_radius=15, border_bottom_left_radius=15)
            pg.draw.circle(screen, color='black', center=(x+5, y+10), radius=2)
            pg.draw.circle(screen, color='black',
                           center=(x+10, y+10), radius=2)

    # 移动控制

    def head_event(self, event):
        global direction, position
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_LEFT or event.key == pg.K_a) and direction != right:
                direction = left
            elif (event.key == pg.K_RIGHT or event.key == pg.K_d) and direction != left:
                direction = right
            elif (event.key == pg.K_UP or event.key == pg.K_w) and direction != down:
                direction = up
            elif (event.key == pg.K_DOWN or event.key == pg.K_s) and direction != up:
                direction = down

    def move(self):
        global position, body_list
        body_list.append([position[0], position[1]])
        if len(body_list) > length_of_snake:
            body_list.pop(0)
        position[0] += direction[0]
        position[1] += direction[1]

    # 身体
    def draw_snake_body(self):
        for body_positon in body_list:
            x = body_positon[0]
            y = body_positon[1]
            body = pg.draw.rect(screen, color=('snow'), rect=(
                x, y, 15, 15), width=10)

    # 吃食物并生长

    def eat_food(self):
        global length_of_snake, number_of_food, speed
        if number_of_food != 0:
            food_rect = pg.Rect(food_pos[0]-7, food_pos[1]-7, 14, 14)
            if head.colliderect(food_rect):
                length_of_snake += 5
                number_of_food -= 1
                speed += 4
                pg.time.wait(100)


class food():
    def draw_food(self):
        global number_of_food
        if number_of_food == 0:
            food_pos[0] = rd.randint(20, WIDTH-20)
            food_pos[1] = rd.randint(20, HEIGHT-20)
            number_of_food += 1
        if number_of_food == 1:
            pg.draw.circle(screen, color='red', center=(
                food_pos[0], food_pos[1]), radius=7)


def is_game_over():
    global game_state
    x, y = position[0], position[1]
    if x > WIDTH or y > HEIGHT or x < 0 or y < 0:
        game_state = 'game_over'
    for body_positon in body_list:
        if body_positon == position:
            game_state = 'game_over'


def reset_game():
    """重置游戏所有变量"""
    global position, direction, body_list, length_of_snake
    global number_of_food, food_pos, game_state, speed
    speed = 4
    position = [WIDTH//2, HEIGHT//2]
    direction = right
    body_list = []
    length_of_snake = 10
    number_of_food = 0
    food_pos = [0, 0]
    game_state = "playing"


def draw_game_over_screen():
    """绘制游戏结束界面"""
    screen.fill('black')

    # 游戏结束标题
    font_large = pg.font.Font(None, 72)
    text_game_over = font_large.render('GAME OVER', True, 'red')
    screen.blit(text_game_over, (WIDTH//2 -
                text_game_over.get_width()//2, 200))

    # 分数显示
    font_medium = pg.font.Font(None, 48)
    text_score = font_medium.render(f'Score: {length_of_snake}', True, 'white')
    screen.blit(text_score, (WIDTH//2 - text_score.get_width()//2, 300))

    # 重新开始按钮
    restart_button = pg.Rect(WIDTH//2 - 150, 400, 300, 60)
    pg.draw.rect(screen, 'green', restart_button, border_radius=15)
    font_button = pg.font.Font(None, 36)
    text_restart = font_button.render('Press R to Restart', True, 'white')
    screen.blit(text_restart, (WIDTH//2 - text_restart.get_width()//2, 415))

    # 退出按钮
    quit_button = pg.Rect(WIDTH//2 - 150, 500, 300, 60)
    pg.draw.rect(screen, 'red', quit_button, border_radius=15)
    text_quit = font_button.render('Press Q to Quit', True, 'white')
    screen.blit(text_quit, (WIDTH//2 - text_quit.get_width()//2, 515))

    pg.display.update()


def handle_game_over_input(event):
    """处理游戏结束界面的输入"""
    global running, game_state

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_r:
            reset_game()
        elif event.key == pg.K_q:
            running = False
    elif event.type == pg.MOUSEBUTTONDOWN:
        # 添加鼠标点击按钮的功能
        mouse_pos = pg.mouse.get_pos()
        restart_button = pg.Rect(WIDTH//2 - 150, 400, 300, 60)
        quit_button = pg.Rect(WIDTH//2 - 150, 500, 300, 60)

        if restart_button.collidepoint(mouse_pos):
            reset_game()
        elif quit_button.collidepoint(mouse_pos):
            running = False


s = snake()
f = food()

clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if game_state == "playing":
            s.head_event(event)
        elif game_state == "game_over":
            handle_game_over_input(event)

    if game_state == "playing":
        s.move()
        screen.fill('black')
        f.draw_food()
        s.draw_snake_body()
        s.draw_snake_head()
        s.eat_food()
        is_game_over()
        pg.display.update()
        clock.tick(46+speed)

    elif game_state == "game_over":
        draw_game_over_screen()
        clock.tick(10)

pg.quit()
