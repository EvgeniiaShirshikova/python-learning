# option 1
# from my_functions import sum_ignore_non_numbers, is_triangle, average, common_strings

# option 2
# import my_functions
# print(my_functions.is_triangle(5, 6, 8))

# option 3
# import my_functions as func
# print(func.is_triangle(5, 6, 8))

# option 4
# from my_functions import *
# print(is_triangle(5, 6, 8))


# Домашнее задание (занятие 6)

# 1
# Модуль.
#
# - Перенесите ваши функции из прошлого домашнего задания в отдельный
# файл и импортируйте их в основной (исполняемый) файл.
# - Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.
#
# 2
#
# Анонимная функция 🎭.
#
# - Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
# Функция должна возвращать x, возведенное в степень y.
#

pow = lambda x,y: x**y
print(pow(3,2))

# 3
# Змея 🐍.
#
# - Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
# - Функция должна создать новую строку, где все гласные буквы
# aeiouyAEIOUY в строке text дублируются.
# - Например, такой вызовы функции snake_talk(“Harry”) должен вернуть
# строку “Haaryy”.

def snake_talk(text: str) -> str:
    result = ""
    for char in text:
        result += char
        if char in "aeiouyAEIOUY":
            result +=char
    return result

print(snake_talk("Harry"))
