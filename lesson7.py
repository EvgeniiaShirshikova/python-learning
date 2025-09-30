# Домашнее задание (Занятие 7)
# 1
# Прямоугольник
# Создайте класс Rectangle, который принимает ширину и высоту прямоугольника при
# создании и должен иметь соответствующие атрибуты width и height (целые числа).
# Создайте метод area(), который возвращает площадь прямоугольника.
# Создайте метод perimeter(), который возвращает периметр прямоугольника.
# Пример:
# rect = Rectangle(2, 4)
# a = rect.area() # Вернул 8
# p = rect.perimeter() # Вернул 12
#
#
# class Rectangle:

#   def __init__(self, width: int, height: int):
#       self.width = width
#       self.height = height

#
#   def area(self):
#       return self.width * self.height

#   def perimeter(self):
#       return (self.width + self.height) * 2
#
# rect = Rectangle(2, 4)
# a = rect.area() # Вернул 8
# p = rect.perimeter() # Вернул 12
# print(a)
# print(p)

# 2
# Автомобиль
# Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную
# скорость (max_speed) в виде целого числа при создании.
# Также при инициализации (в теле __init__) экземпляра Car должен быть автоматически создан
# атрибут speed, равный 0 (текущая скорость автомобиля).
#
# Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля.
# Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость
# автомобиля не должна превышать max_speed, если вызывается accelerate() при максимальной скорости,
# то скорость не должна увеличиваться.
# Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом скорость автомобиля
# не может быть меньше 0. Если вызывается метод brake() при скорости равной 0, то скорость
# не должна уменьшаться.
# Пример:
# my_toyota = Car("Toyota", 180)
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 3
#
#
# class Car:
#
#     def __init__(self, make: str, max_speed: int):
#         self.speed = 0
#         self.make = make
#         self.max_speed = max_speed
#
#
#     def display_speed(self):
#         print(self.speed)
#
#     def accelerate(self):
#         if self.speed <= (self.max_speed - 10):
#             self.speed +=10
#         elif (self.max_speed - 10) < self.speed < self.max_speed:
#             self.speed = self.max_speed
#
#     def brake(self):
#         if self.speed >= 10:
#                 self.speed -= 10
#         elif 0 < self.speed < 10:
#                 self.speed = 0
#
#
#
#
#
# my_toyota = Car("Toyota", 180)
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 3
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 3
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 3
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 3
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
# my_toyota.accelerate()
# my_toyota.display_speed()
#

#
# Повторение прошлого материала.
# Ответьте на следующие вопросы:
# Что такое and, or и not? Приведите пример их использования.
# Что такое цикл? Чем отличается for от while?
# Что такое функция? Зачем она нужна?


# Task 8. Factorial Calculation (loops, recursion)
# Tasks:
# Write two functions to calculate the factorial of a number:
# One using loops.
# One using recursion.
# Example:
# factorial(5) # 120
#
# def factorial_loop(n):
#     result = 1
#     if n == 0 or n == 1:
#         return 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
# print(factorial_loop(5))

# def factorial_recursion(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursion(n - 1)
#
# print(factorial_recursion(5))

# FizzBuzz Task Description:
#
# Write a program that prints the numbers from 1 to 100, but:
#
# For numbers divisible by 3, print "Fizz" instead of the number.
#
# For numbers divisible by 5, print "Buzz" instead of the number.
#
# For numbers divisible by both 3 and 5, print "FizzBuzz".
#
# For all other numbers, print the number itself.

# def print_fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 5 == 0:
#             print("Buzz")
#         elif i % 3 == 0 :
#             print("Fizz")
#         else:
#             print(i)
#
# print_fizzbuzz()
#
# FizzBuzzWoof rules:
#
# If a number is divisible by 3, print "Fizz".
#
# If divisible by 5, print "Buzz".
#
# If divisible by 7, print "Woof".
#
# If divisible by multiple numbers, concatenate the words (e.g., 15 → "FizzBuzz", 21 → "FizzWoof", 105 → "FizzBuzzWoof").
#
# Otherwise, print the number itself.

def print_fizzbuzzwoof():
    for i in range(1, 106):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            print("FizzBuzzWoff")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 7 == 0:
            print("FizzWoff")
        elif i % 5 == 0 and i % 7 == 0:
            print("BuzzWoff")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 :
            print("Fizz")
        else:
            print(i)

print_fizzbuzzwoof()