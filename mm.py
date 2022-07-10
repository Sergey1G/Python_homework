# a = int(input())
# b = int(input())
# if a ** 2 == b or b ** 2 == a:
#     print('yes')
# else:
#     print('no')


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# max_number = a
# if max_number < b:
#     max_number = b
# if max_number < c:
#     max_number = c
# if max_number < d:
#     max_number = d
# if max_number < e:
#     max_number = e
# print(max_number)


# a = list(map(int, input().split()))
# max_number = a[0]
# for i in a:
#     if i > max_number:
#         max_number = i
# print(max_number)

# 
# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# n = int(input())
# if ((n % 5 == 0 and n % 10 == 0) or (n % 15 == 0)) and n % 30 != 0:
#     print('yes')
# else:
#     print('no')

# Грабер Мартин "SQL для простых смертных"
# sql-ex.ru (100 задачек)

# аналитик python(numpy, pandas, maplotlib, seaborn, sklearn)




# Будем называть числа круглыми, если они содержат в своей записи только цифры 0 и 5. 
# Составим последовательность неотрицательных целых круглых чисел в порядке возрастания: 0, 5, 50, 55, 500, 505 и так далее.

# Написать программу, которая находит K-е по порядку в этой последовательности круглое число.

# a = int(str((bin(int(input()) - 1)))[2:])*5
# print(a)





