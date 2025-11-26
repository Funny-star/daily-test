def print_rhombus(rows):
    board = [[0]*rows for _ in range(rows)]
    # 先判断rows的奇偶,再分别打印
    if rows % 2 == 0:
        for i in range(rows):
            board[i][rows//2-i-1] = '*'
            board[i][-rows//2+i] = '*'
    elif rows % 2 != 0:
        for i in range(rows//2+1):
            board[i][rows//2-i] = '*'
            board[i][-rows//2+i] = '*'
        for i in range(rows//2):
            board[-i-1][rows//2-i] = '*'
            board[-i-1][-rows//2+i] = '*'

    for i in board:
        for j in i:
            print((j if j != 0 else ' '), end='\t')
        print()


n = input('输入行数')
try:
    if (n := int(n)) <= 0:
        raise ValueError
except ValueError:
    print('请输入正整数')
    exit()


print_rhombus(n)
