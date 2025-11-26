
def init_board():
    return [[0]*10 for _ in range(10)]


def print_board(board):
    for row in board:
        for i in row:
            print((i if i != 0 else '-'), end='\t')
        print()


# 当贪吃蛇转向时需要其头部的坐标
snake_head = 'B-'
snake_body = 'O'


def find_snake_head(board):
    return [(j, i) for j in range(10) for i in range(10) if i == 'B-']


def move_right(board, head_position, len_of_snake):
    # 先动头
    board[head_position[0]][head_position[1]], board[head_position[0]][head_position[1] +
                                                                       1] = board[head_position[0]][head_position[1]+1], board[head_position[0]][head_position[1]]
    # 再动身体
