import random
import os

# 完成对棋盘的初始化


def init_board():
    board = [[0] * 4 for _ in range(4)]
    board = add_new_num(board)
    board = add_new_num(board)
    return board

# 打印棋盘


def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    for i in board:
        for j in i:
            print((j if j != 0 else "-"), end="\t")
        print()
    print()

# 随机添加一个 2 或 4


def add_new_num(board):
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.9 else 4
    return board

# 向左：压缩


def compress(row):
    new_row = [num for num in row if num != 0]
    while len(new_row) < 4:
        new_row.append(0)
    return new_row

# 向左：合并


def merge(row):
    for i in range(3):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return row

# 向左：处理一行


def process_row(row):
    row = compress(row)
    row = merge(row)
    row = compress(row)
    return row

# 向左移动


def move_left(board):
    return [process_row(row) for row in board]

# 向右移动


def move_right(board):
    board = [row[::-1] for row in board]
    board = move_left(board)
    return [row[::-1] for row in board]

# 逆时针旋转


def rotate_counterclockwise(board):
    return [[board[j][3 - i] for j in range(4)] for i in range(4)]

# 顺时针旋转


def rotate_clockwise(board):
    return [[board[3 - j][i] for j in range(4)] for i in range(4)]

# 向上移动


def move_up(board):
    board = rotate_counterclockwise(board)
    board = move_left(board)
    return rotate_clockwise(board)

# 向下移动


def move_down(board):
    board = rotate_clockwise(board)
    board = move_left(board)
    return rotate_counterclockwise(board)

# 判断是否结束


def is_game_over(board):
    # 1. 是否还有空格
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
    # 2. 是否还能合并
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                return False
    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i+1][j]:
                return False
    return True

# 游戏主循环


def game():
    board = init_board()
    print_board(board)

    while True:
        # 等待用户输入
        user_input = input("请输入指令(W/A/S/D/Q):").lower()
        if user_input == "q":
            break

        if user_input == "a":
            new_board = move_left(board)
        elif user_input == "d":
            new_board = move_right(board)
        elif user_input == "w":
            new_board = move_up(board)
        elif user_input == "s":
            new_board = move_down(board)
        else:
            print("输入错误，请重新输入。")
            continue

        # 如果棋盘有变化，添加新数字
        if new_board != board:
            board = add_new_num(new_board)

        print_board(board)

        if is_game_over(board):
            print("没有可移动的空间，游戏结束。")
            break


if __name__ == "__main__":
    game()
