# def swap_values():
#     a , b = b , a
#     return (a , b)

# example_dict = {'a': 100, 'b': 200, 'c': 300}


# def sum_of_dict_values(dict_1):
#     num1 = 0
#     for i in dict_1:
#         print(i)

#         num1 += dict_1[i]
#     return num1


# print(sum_of_dict_values(example_dict))


# num_1 = input('亲，输入一个数字哟')

# try:
#     num_1 = int(num_1)
# except ValueError:
#     print("请输入整数")


# def sum_of_reciprocal_series(n):
#     sum = 0
#     if n % 2 == 0:
#         for i in range(2, n + 1, 2):
#             sum += 1/i

#     else:
#         for i in range(1, n + 1, 2):
#             sum += 1/i

#     return sum


#


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


year = check_number(input('请输入年份'))
month = check_number(input('请输入月份'))
day = check_number(input('请输入日期'))


def num_of_day(year, month, day):

    result = 0
    for i in range(1, month):
        if i == 2 and year % 4 != 0:
            result += 28
        elif i == 2 and year % 4 == 0:
            result += 29
        elif 2 < i <= 7 or i == 1:
            if i % 2 == 0:
                result += 30
            if i % 2 == 1:
                result += 31

        elif 12 >= i > 7:
            if i % 2 == 0:
                result += 31
            if i % 2 == 1:
                result += 30

    result += day
    return result


print(num_of_day(int(year), int(month), int(day)))
