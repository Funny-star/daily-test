import sys


def change_str(a_str, number):
    new_str_1 = ''
    new_str_2 = ''
    if number >= len(a_str):
        print('数字太大了')
        sys.exit()
    else:
        for i in range(number):
            new_str_1 += (a_str[i])
            new_str_1 = new_str_1[::-1]
            new_str_2 += (a_str[-i-1])
        # print(new_str_1)
        # print(new_str_2)
        if number <= len(a_str)//2:
            print(a_str[number:-number:1])
            print(new_str_1 + a_str[number:-number:1] + new_str_2)
        else:
            print(new_str_1 + new_str_2)


a_str = input('请输入字符串')
number = input('请输入一个数字')
try:
    number = int(number)
except:
    print('请输入数字')
    sys.exit()
change_str(a_str, int(number))
