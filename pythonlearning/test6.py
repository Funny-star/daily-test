import random


def init_lit():  # 生成一个原始列表
    lit = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]

    ]

    return lit


lit = init_lit()


def randomly_generated():  # 随机生成2或4
    random_flo = random.random()
    if random_flo <= 0.9:
        num_1 = 2
    else:
        num_1 = 4
    return num_1


num_1 = randomly_generated()


def find_0():  # 检测棋盘中为零的坐标
    empty_plot = [(i, j)for i in range(4)
                  for j in range(4) if lit[i][j] == 0]

    return empty_plot


empty_plot = find_0()


def print_board():  # 打印一个棋盘
    for row in lit:
        for i in row:
            print(i, end='\t')  # 制表符使数字对齐
        print()


def replace_0():  # 将0替换为随机生成的2或4
    random_0 = random.choice(empty_plot)
    lit[random_0[0]][random_0[1]] = num_1
    return lit


def compressed():
    for row in range(4):
        for i in range(3):
            if lit[row][i] == 0 and lit[row][i+1] != 0:
                lit[row][i], lit[row][i+1] = lit[row][i+1], lit[row][i]
            elif lit[row][i] == 0 and lit[row][i+1] == 0 or lit[row][i] != 0 and lit[row][i+1] == 0:
                continue
    return lit


def merger_left():
    for row in range(4):
        for i in range(3):
            if lit[row][i] == lit[row][i+1]:
                lit[row][i] += lit[row][i+1]
                lit[row][i+1] = 0
    return lit


replace_0()
replace_0()
print_board()


while 1 == 1:
    direction = input('Direction:')
    if direction == 'a':
        compressed()
        merger_left()
        compressed()
        replace_0()
        print_board()
