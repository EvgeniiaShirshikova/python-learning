# Четное или нечетное?
# Создать переменную n, значение которой определяется через ввод данных с клавиатуры.
# Если n является четным числом, то вывести на экран слово “четное”.
# Если n является нечетным числом, то вывести на экран слово “нечетное”.

# n = int(input("Input the number: "))
#
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# print("even" if n % 2 == 0 else "odd")

#Какой сегодня день?
#Создать переменную day, значение которой определяется через ввод данных с клавиатуры.
#Если значение day равно “суббота” или “воскресенье”, то вывести на экран строку “Сегодня выходной!”.
#Если значение day равно “среда”, то вывести на экран “Мне сегодня к стоматологу в 15:30”.
#Во всех остальных случая выводить на экран “Сегодня обычный день.”.

# day = input("What day is today? ").lower()
#
# if day == "saturday" or day == "sunday":
#     print("Today is weekend!")
# elif day == "wednesday":
#     print("Today is my dental appointment")
# else :
#     print("Today is just a day")

# match day:
#     case "wednesday":
#         print("Today is my dental appointment")
#     case ("saturday" | "sunday"):
#         print("Today is weekend!")
#     case ("tuesday" | "thursday" | "friday"):
#         print("Today is just a day")
#     case _:
#         print("Sorry, I don't understand that.")

# Эхо.
# Создать переменную n, значение которой определяется через ввод данных с клавиатуры (целое число).
# Создать переменную text, значение которой определяется через ввод данных с клавиатуры (строка).
# Программа должна вывести вашу строку text на экран n-раз. Если вы ввели 3, а затем “Ау”, то результат должен быть:
# Ау
# Ау
# Ау

# n = int(input("input your number: "))
# text = str(input("input your text: ") + "\n")
# print(n * text)

# Сколько гласных букв? Создать переменную message, значение которой определяется
# через ввод данных с клавиатуры. Программа должна вывести на экран
# количество гласных букв в строке message.Например, если
# была введена строка “Мой кот уверен, что клавиатура – это специально для него купленный массажер”, то
# программа должна вывести 26.
# Подразумевается, что подсчитываться должна только кириллица, то есть буквы а, о, у, ы и так далее.

# message = input("Enter your message: ")
# vowels = "аяиюэыоуеё"
# count = 0
# for letter in message:
#     if letter.lower() in vowels:
#         count += 1
#
# print(count)


# Сумма чисел.
# Программа должна запрашивать у пользователя ввести число с клавиатуры. После того как пользователь ввел число
# (пользователь должен вводить только целые числа), она должна опять попросить его ввести число и так
# должно продолжаться пока пользователь не введет отрицательное число. Как только пользователь ввел отрицательное число,
# программа должна вывести сумму всех чисел, которые он вводил до этого (не включая отрицательное) и завершиться.
# Например, если ввод пользователя выглядит так:
# 43
# 1
# 345
# -1
#
# То программа должна вывести:
# 389

# n = 0
# count = 0
# while n >= 0:
#     count += n
#     n = int(input("Enter an integer number: "))
# else:
#     print(count)

# Positive, Negative, or Zero
# Create a variable n, whose value is determined by keyboard input.
# If n is greater than zero, print "Positive".
# If n is less than zero, print "Negative".
# If n equals zero, print "Zero".

# n = int(input("Enter a number: "))
# if n > 0:
#     print("positive")
# elif n < 0:
#     print("negative")
# else:
#     print("zero")
#
# 2. Grade by Score
# The user enters a score (0–100).
# If the score is greater than or equal to 90 — print "Excellent".
# If from 70 to 89 — print "Good".
# If from 50 to 69 — print "Satisfactory".
# Otherwise — print "Unsatisfactory".

# n = int(input("Enter your score: "))
#
# if n >= 90:
#     print("Excellent")
# elif 70 <= n < 90:
#     print("Good")
# elif 50 <= n < 70:
#     print("Satisfactory")
# elif 0 <= n < 50:
#     print("Unsatisfactory")
# else:
#     print("Try again")

# 3. Multiplication Table
# The user enters a number n.
# Display the multiplication table for n from 1 to 10 (inclusive) using a for loop.
#
# Example for n = 3:
#
# 3 × 1 = 3
# 3 × 2 = 6
# ...
# 3 × 10 = 30

n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n * i}")