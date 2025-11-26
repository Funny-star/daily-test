import os
import time
import threading
import keyboard

SNAKE_BODY = ["o"]
INIT_POSITION = [50, 15]
INIT_DIRECTION = 'd'

direction = INIT_DIRECTION


def print_snake(position):
    '''
    对蛇进行打印
    '''
    time.sleep(0.08)
    os.system('cls')
    x = position[0]
    y = position[1]
    for _ in range(y-1):
        print(' ')
    print(' '*(x-1), SNAKE_BODY[0])
    for _ in range(y-1):
        print(' ')


def move(position, direction):

    if direction == 'd':
        position[0] += 1
        return position
    if direction == 'a':
        position[0] -= 1
        return position
    if direction == 'w':
        position[1] -= 1
        return position
    if direction == 's':
        position[1] += 1
        return position


def keyboard_control():
    global direction
    while True:
        if keyboard.is_pressed('w') and direction != 's':
            direction = 'w'
        elif keyboard.is_pressed('d') and direction != 'a':
            direction = 'd'
        elif keyboard.is_pressed('a') and direction != 'd':
            direction = 'a'
        elif keyboard.is_pressed('s') and direction != 'w':
            direction = 's'
        time.sleep(0.05)


def is_game_over(position):
    if position[0] == 100 or position[0] == 0:
        return False
    elif position[1] == 30 or position[1] == 0:
        return False
    else:
        return True


def game():
    position = INIT_POSITION.copy()
    global direction

    print_snake(INIT_POSITION)

    update_direction = threading.Thread(target=keyboard_control)
    update_direction.daemon = True
    update_direction.start()

    while True:

        print_snake(position)
        position = move(position, direction)
        if is_game_over(position):
            continue
        else:
            print("game over")
            break


game()
