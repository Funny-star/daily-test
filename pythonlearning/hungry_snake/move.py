import os
import time


def init_board():
    return [[0]*10 for _ in range(10)]


def print_board(board):
    for row in board:
        for i in row:
            print((i if i != 0 else '-'), end='\t')
        print()


# print_board(init_board())


snake = "O"
board = init_board()


def move(board, snake):
    for i in range(4):
        os.system('cls')
        board[0][i] = snake
        print_board(board)
    time.sleep(1)
    for i in range(6):
        os.system('cls')
        board[0][i+4] = snake
        board[0][i] = 0
        print_board(board)
        time.sleep(0.5)


move(board, snake)
