
class board:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def print_board(self):
    #     for _ in range(self.x):
    #         print('*', end='')
    #     for _ in range(self.y-2):
    #         print('')
    #     for _ in range(self.x):
    #         print('*', end='')


# init_board = board(100, 30)
# init_board.print_board()


class snake(board):

    def __init__(self, body, position):
        self.body = body
        self.position = position
