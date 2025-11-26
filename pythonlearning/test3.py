lit = [8, 2, 3, 4, 45, 5, 7]


def num(n):
    for i in range(0, n-1):
        for j in range(0, n-1):
            if lit[j] > lit[j+1]:
                lit[j], lit[j+1] = lit[j+1], lit[j]
            else:
                continue

    return lit


print(num(len(lit)))
