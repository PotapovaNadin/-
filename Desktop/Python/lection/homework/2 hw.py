# Задача 1. Напишите программу, которая принимает на вход 
# вещественное или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.
# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# n = input('Введите число: ')
# sum = 0
# for a in n:
#     if a != '.':
#         sum += int(a)
# print(sum)

# try:
#     n = float(input('Введите число: '))
#     sum = 0
#     while float(n) - int(n) != 0:
#         n *= 10
#     while (n > 0):
#         sum += int(n) % 10
#         n //= 10
#     print(sum)
# except:
#     print('Введите число: ')


# Задача 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# *Пример:*

# - пусть N = 4, 
# тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# try:
#     n = int(input('Введите целое натуральное число: '))
#     def find_fact(n):
#         factorial = 1
#         for i in range(n):
#             i += 1
#             factorial *= i
#             print(factorial, end =' ')

#     find_fact(n)

# except:
#     print('Введите целое число: ')


# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой. 
# COUNT или FIND или SPLIT нельзя юзать! говорил же на семинаре.


# first_st = input('Введите первую строку: ')
# second_st = input('Введите вторую строку: ')
# score = 0

# for i in second_st:
#     if i in first_st:
#         score +=1
# print(score)

# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, 
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

# import math

# n = int(input('Введите целое число мерности пространства : '))
# a = []
# b = []
# def create_lists(n):
#     for i in range(n):
#         a_number = int(input(f'Введите измерение координаты первой точки {i+1} '))
#         a.append(a_number)
#         b_number = int(input(f'Введите измерение координаты второй точки {i+1} '))
#         b.append(b_number)
#     return(a, b)

# list_of_numbers = create_lists(n)
# print(list_of_numbers)

# def find_distance(a, b, n):
#     sum = 0
#     for i in range(n):
#         sum += (a[i] - b[i])**2
#     return(math.sqrt(sum))

# distance = find_distance(a, b, n)
# print(distance)

#  (3,6,8); B (2,1,-7), -> 15.84
#  (7,-5, 0); B (1,-1,9) -> 11.53 


# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, 
# проверяем это утверждение 100 раз, с помощью модуля time выводим на экран, 
# сколько времени отработала программа.