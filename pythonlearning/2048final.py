import random
import os

score = 0


def init_board():
    '''
    创建初始棋盘
    '''
    board = [[0]*4 for _ in range(4)]
    return board


def print_board(board):
    '''
    打印棋盘
    '''
    os.system('cls')
    for row in board:
        for i in row:
            print((i if i != 0 else '-'), end='\t')
        print()
    print("\n" + " " * 12 + str(score))


def find_0(board):
    '''
    找到零的位置
    '''
    empty = [(i, j)for i in range(4) for j in range(4) if board[i][j] == 0]
    return empty


def random_number():
    '''
    生成2或4
    '''
    return 2 if random.random() <= 0.9 else 4


def replace_0(board):
    '''
    替换0
    '''
    space_position = random.choice(find_0(board))
    board[space_position[0]][space_position[1]] = random_number()
    return board


def compress(row):
    '''
    压缩函数
    '''
    compress_list = [i for i in row if i != 0]
    while len(compress_list) < 4:
        compress_list.append(0)
    return compress_list


def merge(row):
    '''
    合并函数
    '''
    global score
    for i in range(3):
        if row[i] != 0 and row[i] == row[i + 1]:
            score += sum_score(row[i], row[i+1])
            row[i] += row[i + 1]
            row[i + 1] = 0
    return row


def move_left(board):
    '''
    向左
    '''
    new_board = []
    for row in board:
        row = compress(row)
        row = merge(row)
        row = compress(row)
        new_board.append(row)
    return new_board


def move_right(board):
    '''
    向右
    '''
    board = [row[::-1] for row in board]
    board = move_left(board)
    return [row[::-1] for row in board]


def move_up(board):
    '''
    向上
    '''
    for _ in range(3):
        board = rotate_counterclockwise(board)
    board = move_left(board)
    board = rotate_counterclockwise(board)
    return board


def move_down(board):
    '''
    向下
    '''
    board = move_left(
        rotate_counterclockwise(board))
    for _ in range(3):
        board = rotate_counterclockwise(board)
    return board


def rotate_counterclockwise(board):
    '''
    逆时针旋转棋盘90°
    '''
    temporary_board = []
    for i in range(4):
        new_row = []
        for row in range(3, -1, -1):
            new_row.append(board[row][i])
        temporary_board.append(new_row)
    return temporary_board


def is_game_over(board):
    # 检测是否无空位
    empty = find_0(board)
    if len(empty) != 0:
        return False
    # 检测是否有横向相邻数相等
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                return False
    # 检测是否有纵向相邻数相等
    for i in range(4):
        for j in range(3):
            if board[j][i] == board[j+1][i]:
                return False
    return True


def sum_score(a, b):
    score = a + b
    return score


'''
本体
'''


def game():
    global score
    board = init_board()
    board = replace_0(board)
    board = replace_0(board)
    print_board(board)
    print('\n请输入 W A S D 控制方向')

    while True:
        temporary_board = board
        direction = input('\nDirection:')
        direction = direction.lower()
        if direction == 'a':
            temporary_board = move_left(temporary_board)

        elif direction == 's':
            temporary_board = move_down(temporary_board)

        elif direction == 'd':
            temporary_board = move_right(temporary_board)

        elif direction == 'w':
            temporary_board = move_up(temporary_board)

        if board != temporary_board:
            board = replace_0(temporary_board)
        print_board(board)

        if is_game_over(board):
            print('Game Over')


game()
