# num = 100
# name = "Алексей"
# first_number = 1
# my_text = "text"
# phone_number = "Hi!"
#
my_name = "Jean"

print("Hi, my name is " + my_name + ".")
print("Hi, my name is", my_name, end=".\n")
print(f"Hi, my name is {my_name}.")

# Создать переменную name, значение которой определяется через ввод данных с клавиатуры.
# Создать переменную surname, значение которой определяется через ввод данных с клавиатуры.
# Вывести на экран строку "Привет, меня зовут <имя> <фамилия>.". Значение переменных name и surname должно быть отформатировано
# к корректному виду. Например, если с клавиатуры вводятся строки "еЛеНА" и "поПОВА", то результат должен быть
# "Привет, меня зовут Елена Попова."

name = input("Enter your name: ")
surname = input("Enter your surname: ")
print("Hi, my name is " + name.title() + " " + surname.title() + ".")
print(f"Hi, my name is {name.title()} {surname.title()}.")

# Создать переменную a, значение которой определяется через ввод данных с клавиатуры.
# Создать переменную b, значение которой определяется через ввод данных с клавиатуры.
# Вывести на экран сумму двух введенных чисел, если для a было введено 123, а для b 431,
# то на экран должно быть выведено 554.

a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

print(a + b)
