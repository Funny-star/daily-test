# a = [939, 3929, 292, 529, 29529, 598, 19]
# max_num = a[0]
# min_num = a[0]

# for num in a:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print(max_num)
# print(min_num)


# user_input = input(" 请输入：")

# a = ""

# for i in range(len(user_input)-1 , -1 , -1):
#     a += user_input[i]

# if a == user_input:
#     print('true')
# else:
#     print('false')


lit = {'num1': 10, 'num2': 20, 'num3': 30}
new_update = {'num4': 40, 'num5': 50}
lit.update(new_update)
print(lit)
