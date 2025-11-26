
# # lv0
# NUMBER = [1, 2, 5, 17, 520, 4399]
# result = []

# for i in NUMBER:
#     if i % 2 == 1:
#         result.append(i*2)
#     else:
#         result.append(i)

# print(result)

# #lv1
# import math

# number_list = [1, 3, 5, 6, 8]
# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))


# results = []

# for i, num1 in enumerate(number_list):

#     for j, num2 in enumerate(number_list):

#         for k, num3 in enumerate(number_list):
#             if i < j < k:
#                 if abs(num1-num2) <= a and abs(num2-num3) <= b and abs(num1-num3) <= c:
#                     result = [num1, num2, num3]
#                     results.append(result)
#                     print(result)

# print(f"共有{len(results)}个结果")


# #lv2
# class Animal:
#     def __init__(self, name):
#         self._name = name  # 封装：保护属性

#     def speak(self):
#         return "动物发出声音"

#     def get_name(self):
#         return self._name

# # 继承


# class Dog(Animal):
#     def speak(self):  # 多态
#         return "汪汪汪！"


# def animal_speak(animal):  # 多态
#     print(f"{animal.get_name()}:{animal.speak()}")


# dog = Dog("小黑")


# # 多态
# animal_speak(dog)  # 输出：小黑：汪汪汪！

# #lv3
# import _2048

# _2048.game()
