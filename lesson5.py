# 1
# Продвинутый sum.
# Встроенная функция sum() в python вызывает ошибку, если один из элементов последовательности не является числом,
# например sum([1, 2, ‘A’]).
# Напишите функцию sum_ignore_non_numbers(), которая имеет один параметр items (список или кортеж).
# Функция должна вернуть сумму всех чисел (int, float) в переданной последовательности.
# При этом все нечисловые значения должны игнорироваться.
# Если чисел нет, то функция должна вернуть 0.
# Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3
from operator import truediv


# def sum_ignore_non_numbers(items):
#     total = 0
#     for item in items:
#         if type(item) == int or type(item) == float:
#             total += item
#     return total
#
# items = [1, 2, 'A']
#
# print(sum_ignore_non_numbers(items))

# 2
# Треугольник.
# Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
# Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон треугольника.
# Функция должна возвращать True, если треугольник с переданными сторонами может существовать, и False в противном случае.
# Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.
#
#

# def is_triangle(a, b, c):
#     if a + b > c and b + c > a and a + c > b:
#         return True
#     else:
#         return False
#
# print(is_triangle(3, 4, 5))


# 3
# Среднее значение.
# Напишите функцию average(), которая принимает произвольное количество позиционных аргументов.
# (Можно передать любое число аргументов).
# Функция должна посчитать среднее арифметическое всех переданных чисел.
# (Представим, что в функцию передаются только числа).
# Если не передать ни одного аргумента, то функция должна вернуть 0.
#
# Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5
#

# def average(*args):
#     if len(args) == 0:
#         return 0
#     else:
#         return sum(args) / len(args)
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8))

# 4
# Общие строки.
# Напишите функцию common_strings(), которая имеет 3 параметра: list1, list2 и ingore_case=True (значение по умолчанию).
# Функция должна вернуть новых список из тех значений, которые встречаются в обоих списках.
# При этом, если ignore_case равен True, то функция должна игнорировать регистр и считать строки “string”
# и “STRING” одинаковыми.  В противном случае функция должна учитывать регистр символов и считать такие строки разными.
# Все строки в результирующем списке должны быть в нижнем регистре.
# Например, существуют 2 списка:
# fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’]
# fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
# То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’, ‘cherry’].
#

# def common_strings(list1, list2, ignore_case = True):
#      new_list = []
#      if ignore_case:
#          list1 = [i.lower() for i in list1]
#          list2 = [i.lower() for i in list2]
#      for item in list1:
#          if item in list2:
#              new_list.append(item)
#      return new_list
#
# fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
# fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
#
# print(common_strings(fruits_1, fruits_2, False))

#
# Повторение прошлого материала.
# Ответьте на следующие вопросы:
# Каким образом можно преобразовать строку в число? А число в строку?
# Для чего нужен elif в условном операторе?
# Что такое бесконечные циклы и как их избегать?
#

# 1
# КаКоЕ-тО вОлНеНиЕ.
#
# Создать переменную text, значение которой определяется через ввод данных с клавиатуры.
# Каждый символ под четным индексом должен быть переведен в верхний регистр, а каждый нечетный в нижний.
# Вывести полученную строку на экран.
#
# Если была введена строка
# “Чтобы продать что-нибудь ненужное, нужно сначала купить что-нибудь ненужное, а у нас денег нет.”,
# то результат должен быть
# “ЧтОбЫ ПрОдАтЬ ЧтО-НиБуДь нЕнУжНоЕ, нУжНо сНаЧаЛа кУпИтЬ ЧтО-НиБуДь нЕнУжНоЕ, а у нАс дЕнЕг нЕт.”

# text = input('Enter a string: ')
# result = ''
#
# for i in range(len(text)):
#     if i % 2 == 0:
#         result += text[i].upper()
#     else:
#         result += text[i].lower()
#
# print(result)

# Task 1. Reverse Words in a String (string manipulation)
# Given:
# sentence = "Python is great for interviews"
# Tasks:
# Reverse the order of words (not the letters).
# Expected output:
# "interviews for great is Python"

# sentence = "Python is great for interveiws".split()
# sentence.reverse()
#
# result = ' '.join(reversed("Python is great for interveiws".split()))
# print(result)

# Task 2. Remove Duplicates from List (sets, lists)
# Given:
# numbers = [1, 2, 2, 3, 4, 4, 5]
# Tasks:
# Remove duplicates without changing the order.
# Expected output:
# [1, 2, 3, 4, 5]

# numbers = [1, 2, 2, 3, 4, 4, 5]
# # Option 1
# # unique_numbers = []
# #
# # for i in numbers:
# #     if i not in unique_numbers:
# #         unique_numbers.append(i)
# # print(unique_numbers)
# #
# # Option 2
# print(list(set(numbers)))

# Task 3. Fibonacci Sequence (loops, logic)
# Tasks:
# Print the first 10 numbers of the Fibonacci sequence.
# Expected output:
# 0 1 1 2 3 5 8 13 21 34

# a = 0
# b = 1
# my_list = [a, b]
#
# while len(my_list) < 10:
#     new_sum = a + b
#     my_list.append(new_sum)
#     a = b
#     b = new_sum
#
# print(my_list)
#
# Task 4. Palindrome Checker (strings, conditions)
# Given:
# word = "racecar"
# Tasks:
# Check if it is a palindrome (reads the same backward and forward).
# Expected output:
# True
# Extra:
# Make it work with a sentence ignoring spaces and case.

word = "racecar"
reversed_word = word[::-1]
print(word == reversed_word)