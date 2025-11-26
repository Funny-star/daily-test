import os
import time


def init_board():
    board = [["( _ )"]*3 for _ in range(3)]
    return board


def print_board(board):
    for i in board:
        for j in i:
            print(f"{j}", end='\t')
        print()


def put_down_chess(board, player):

    x = int(input('请输入横坐标以:'))
    y = int(input('请输入纵坐标以:'))

    if 0 < x < 4 and 0 < y < 4 and board[y-1][x-1] == "( _ )":
        if player % 2 == 1:
            board[y-1][x-1] = '  X'
        elif player % 2 == 0:
            board[y-1][x-1] = '  O'
    else:
        print('坐标不对')
        time.sleep(1)
        return board, False

    return board, True


def is_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "( _ )":
            print('game over')
            return False
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "( _ )":
            print('game over')
            return False
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "( _ )":
        print('game over')
        return False
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != "( _ )":
        print('game over')
        return False
    else:
        return True


def game():

    board = init_board()

    player = 1
    while is_game_over(board):
        os.system('cls')
        print_board(board)
        board, is_valid = put_down_chess(board, player)
        if is_valid:
            player += 1


game()
