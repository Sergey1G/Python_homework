# 17. По двум заданным числам проверять является ли одно квадратом другого
# def square_or_not(a, b):
#     if a == b**2: return f'Число {a} является квадратом числа {b}'
#     elif b == a **2: return f'Число {b} является квадратом числа {a}'
#     else: return 'Ни одно число не является квадратом второго'

# A = int(input('Введите число 1 - '))
# B = int(input('Введите число 2 - '))
# print(square_or_not(A, B))

# 19. Определить номер четверти плоскости, в которой находится точка с 
# координатами Х и У, причем X ≠ 0 и Y ≠ 0
# def find_quatro(c, d):
#     if c > 0 < d: return '1-ая четверть'
#     elif c < 0 < d: return '2-ая четверть'
#     elif c < 0 > d: return '3-ая четверть'
#     elif c > 0 > d: return '4-ая четверть'
#     else: return 'Неверно введены данные. X ≠ 0 и Y ≠ 0'
# C, D = 5, -3
# print(find_quatro(C, D))

# 21. Программа проверяет пятизначное число на палиндромом.
# def polindrom_or_not(e):
#     e = input('Введите пятизначное число - ')
#     temp1 = int(e)
#     if temp1 > 0: temp2 = list(e)
#     else:
#         temp2 = list(e)
#         temp2.pop(0)
#     while len(temp2) == 5:
#         for i in temp2:
#             if temp2[0] == temp2[-1] and temp2[1] == temp2[-2]:
#                 return f'Число {e} является палиндромом'
#             else: 
#                 return f'Число {e} не является палиндромом'
#     else: return 'Неверно задано число.'

# E = None
# print(polindrom_or_not(E))

# 23. Показать таблицу квадратов чисел от 1 до N 
def square_table(g):
    for i in range(1, g+1): 
        print(f'{i} >>> {i**2}')

G = int(input('Введите конечное число - '))
square_table(G)

# Результат 
# 1 >>> 1
# 2 >>> 4
# 3 >>> 9
# 4 >>> 16
# 5 >>> 25
# None - откуда это взялось?   

# 25. Найти сумму чисел от 1 до А
# def sum_find(h):
#     summa = 0
#     for i in range(1, h+1): 
#         summa += i
#     return summa

# H = int(input('Введите конечное число - '))
# print(sum_find(H))

# 27. Определить количество цифр в числе
# def lenght_of_number(j):
#     temp = list(str(j))
#     if j > 0: return len(temp)
#     else:
#         temp.pop(0)
#         return len(temp)

# J = int(input('Введите число - '))
# print(lenght_of_number(J))

# 29. Написать программу вычисления произведения чисел от 1 до N
# def result_of_numbers_multiplication(k):
#     temp = 1
#     for i in range(1, k+1): 
#         temp *= i
#     return temp

# K = int(input('Введите конечное число - '))
# print(result_of_numbers_multiplication(K))




# #18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# x = True 
# y = True
# x = False
# # y = False

# def its_true(a, b):
#     f1 = not (a or b)
#     f2 = not a and not b
#     return f1 == f2

# print(its_true(x,y))

# #20. Задать номер четверти, показать диапазоны для возможных координат
# def quatro(a):
#     if a==1: return 'x > 0 and y > 0'
#     elif a==2: return 'x < 0 and y > 0'
#     elif a==3: return 'x < 0 and y < 0'
#     elif a==4: return 'x > 0 and y < 0'
#     else: 'Неверно указан номер четверти'
# a = int(input('Введите номер четверти - '))
# print(quatro(a))

# #22. Найти расстояние между точками в пространстве 2D/3D

# #A1A2 = ((x2-x1)**2 + (y2-y1)**2))**0.5

def find_AB():
    AB = []
    text = input('введите координаты точки А - ')
    temp = text.split()
    A = list(map(int, temp))
    AB.append(A) 
    text = input('введите координаты точки B - ')
    temp = text.split()
    B = list(map(int, temp))
    AB.append(B)
    return AB
    
def find_distance_AB(AB):
    point1, point2 = AB
    AB_disane = 0
    for i in range(len(point1)):
        AB_temp = (point2[i]-point1[i])**2
        AB_disane += AB_temp
    return AB_disane**0.5
        
AB = find_AB()
print(AB)
print(find_distance_AB(AB))


# # #24. Найти кубы чисел от 1 до N
# # def find_cube(b):
# #     return [n**3 for n in range(1, b)]

# # b = int(input('Введите конечное число - '))
# # print(find_cube(b))
    
# # #26. Возведите число А в натуральную степень B используя цикл
# # def get_number(a, b):
# #     temp = 1
# #     for n in range(b):
# #         temp *= a
# #     return temp

# # A = int(input('введите число - '))
# # B = int(input('Введите степень - '))

# # print(get_number(A, B))

# # #28. Подсчитать сумму цифр в числе
# # def sum_in_number(n):
# #     sum = 0
# #     for i in n:
# #         sum += int(i)
# #     return sum

# # n = list(input('Введите число -'))
# # print(sum_in_number(n))

# # #30. Показать кубы чисел, заканчивающихся на четную цифру
# # def even_cubes(list):
# #     for i in list: 
# #         if i%2 == 0: 
# #             i **= 3
# #             print(f'{i},', end= ' ') 
        
# # numbers = [2, 2, 10, 45, 3, 7, 6, 6]
# # print(numbers)
# # even_cubes(numbers)

Дано число обозначающее день недели. Выяснить является номер дня недели выходным

def weekends_or_not(x):
    if 1 <= x <= 7:
        if 1 <= x <= 5:
            return 'Этот день недели - рабочий'
        else: return 'Ура! Выходной!'
    else: return 'неверно задано число'

l = int(input('Введите число = '))
print(weekends_or_not(l))