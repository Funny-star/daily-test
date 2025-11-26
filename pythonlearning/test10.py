

def determine_prime_numbers(n):
    '''
    判断n是否为质数
    '''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorization(user_number):
    '''
    将用户输出的数字进行因式分解
    '''
    factorization_list = []
    i = 2

    while True:  # 使用i**2 <= n也可

        if determine_prime_numbers(i) and user_number % i == 0:
            factorization_list.append(i)
            user_number //= i  # 使用 / 除法时，结果返回的是浮点数，改为使用 // 整除时，返回值变为整数
            i = 2
            """
            找寻因数并加入结果列表中
            """

        elif determine_prime_numbers(user_number):

            if user_number != 1:
                factorization_list.append(user_number)
            break
            '''
            将计算的最后一个因数加入结果列表，并退出循环
            '''

        else:
            i += 1
            print(i)
            continue
            '''
            改变寻找因数时使用的除数
            '''

    return factorization_list


def check_number(num):
    """
    检查num是否为正整数
    """
    try:
        num = int(num)
    except ValueError:
        print("非整数")
        exit()
    if not num > 0:
        print("请输入正数")
        exit()
    return num


user_number = input("")


result = f'{user_number} = '
factorization_list = factorization(int(check_number(user_number)))


for i in factorization_list:
    result += f'{i} X '
result = result[:-2]
print(result)  # 可简化进函数中
