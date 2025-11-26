def init_board():
    return [[0]*10 for _ in range(10)]


def print_board(board):
    for row in board:
        for i in row:
            print((i if i != 0 else '-'), end='\t')
        print()


# 计算出snake的所有身体的坐标，并先前依次替换，固只需要移动头部及可。
def build_body(len_of_snake):
    return [f'O{i}' for i in range(len_of_snake)]


def find_body(body, board):
    for i in body:
        body_position = {i: (row, j) for row in board for j in row if i == j}


# def move_right(board, head_position):
#     # 先动头
#     board[head_position[0]][head_position[1]], board[head_position[0]][head_position[1] +
#                                                                        1] = board[head_position[0]][head_position[1]+1], board[head_position[0]][head_position[1]]


board = init_board()
for i in range(4):
    board[0][i] = build_body(5)[i]
print_board(board)
