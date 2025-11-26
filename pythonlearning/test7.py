import random


def init_board():
    '''
    创造一个初始棋盘
    '''
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    return board


def random_2or4():
    '''
    随机生成2或4
    '''
    random_float = random.random()
    if random_float <= 0.9:
        num_1 = 2
    else:
        num_1 = 4
    return num_1


def print_board(board):
    '''
    打印一个棋盘
    '''
    for row in board:
        for i in row:
            print((i if i != 0 else "-"), end='\t')
        print()


def find_0(board):
    '''
    找到棋盘中的0
    '''
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    return empty


def replace_0(empty, board, num_1):
    '''
    将棋盘中随机位置的零替换为指定数字
    '''
    random_empty = random.choice(empty)
    board[random_empty[0]][random_empty[1]] = num_1
    return board


def compress(row):
    '''
    压缩函数
    '''
    compress_list = [i for i in row if i != 0]
    while len(compress_list) < 4:
        compress_list.append(0)
    return compress_list


def merger(compress_list):
    '''
    合并函数
    '''
    for i in range(3):
        if compress_list[i] == compress_list[i+1] and compress_list[i] != 0:
            compress_list[i] += compress_list[i+1]
            compress_list[i+1] = 0
    new_list = compress_list
    return new_list


# def can_compress(board):
#     for i in range(4):
#         for j in range(3):
#             if board[i][j] == board[i][j+1]:
#                 a = True
#     for j in range(4):
#         for i in range(3):
#             if board[i][j] == board[i+1][j]:
#                 b = True
#     if a != True and b != True:
#         return True


def game():
    board = init_board()
    empty = find_0(board)
    board = replace_0(empty, board, random_2or4())
    board = replace_0(empty, board, random_2or4())
    print_board(board)
    '''
    生成初始棋盘
    '''
    while True:
        new_board = []
        new2_board = []
        new3_board = []
        new4_board = []
        direction = input('Direction:')
        if direction == 'a':
            for row in board:
                new_board.append(compress(merger(compress(row))))
            if new_board == board:
                continue
            board = new_board
            empty = find_0(board)
            board = replace_0(empty, board, random_2or4())
            print_board(board)
        '''
        向左
        '''
        if direction == 'd':
            for row in board:
                row = row[::-1]
                new_board.append(compress(merger(compress(row))))
            for i in range(4):
                new_board[i] = new_board[i][::-1]
            if new_board == board:
                continue
            board = new_board
            empty = find_0(board)
            board = replace_0(empty, board, random_2or4())
            print_board(board)
        '''
        向右
        '''
        if direction == 'w':
            new_board = [[board[j][i] for j in range(4)]for i in range(4)]
            for row in new_board:
                new2_board.append(compress(merger(compress(row))))
            new3_board = [[new2_board[j][i]for j in range(4)]for i in range(4)]
            if new3_board == board:
                continue
            board = new3_board
            empty = find_0(board)
            board = replace_0(empty, board, random_2or4())
            print_board(board)
        '''
        向上
        '''

        if direction == 's':
            new_board = [[board[j][i]
                          for j in range(3, -1, -1)]for i in range(4)]
            for row in new_board:
                new2_board.append(compress(merger(compress(row))))
            new3_board = [[new2_board[j][i]
                           for j in range(4)]for i in range(3, -1, -1)]
            if new3_board == board:
                continue
            board = new3_board
            empty = find_0(board)
            board = replace_0(empty, board, random_2or4())
            print_board(board)
        '''
        向下
        '''
        # c = can_compress(board)
        # lit = find_0(board)
        # if c == True and len(lit) == 0:
        #     print('over')
        #     break


game()
