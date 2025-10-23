# 1
# Интернет-банк
#
# - Создайте класс BankAccount, который принимает имя владельца (name) в
# виде строки и текущее состояние счета (balance) в виде целого числа. Оба
# этих атрибута должны быть _защищенным.
# - Создайте метод deposit(), который принимает 1 аргумент (если не считать
# self, конечно) amount (целое число). Метод должен увеличить текущий
# баланс аккаунта на amount.
# - Создайте метод withdraw(), который принимает 1 аргумент amount (целое
# число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
# денег на счету недостаточно, то метод выводит на экран “Недостаточно
# средств!”.
# - Создайте метод get_balance(), который возвращает текущее значение
# баланса аккаунта.
# Пример:
# account = BankAccount("Maria", 1000)
# account.deposit(700)
# account.withdraw(200)
# print(account.get_balance()) # 1500
#

class BankAccount:
    def __init__(self, name: str, balance: int):
        self._name = name
        self._balance = balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        if self._balance < amount:
            print("Sorry, you don't have enough money")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance()) # 1500

# 2
# Овердрафт
#
# - Создайте класс OverdraftAccount, унаследованный от вашего класса
# BankAccount из предыдущей задачи.
# - Переопределите существующий метод withdraw(), но теперь, если баланс
# аккаунта меньше или равен 0, то это не выводит на экран сообщение
# “Недостаточно средств!”, а уменьшает баланс в минус.
# Пример:
# jack_account = OverdraftAccount("Jack", 0)
# jack_account.withdraw(100)
# jack_account.withdraw(100)
# jack_account.withdraw(100)
# print(jack_account.get_balance()) # -300
#

class OverdraftAccount(BankAccount):
    def withdraw(self, amount: int):
        self._balance -= amount

jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300

# Повторение прошлого материала.
#
# Ответьте на следующие вопросы:
# 1. Зачем нужен метод copy() у списка?
# 2. Что такое словарь и чем он отличается от списка или кортежа?
# 3. Как создается строка документации у функции?
#
# 1
#
# users = [
# {'id': 345324, 'name': 'Alice', 'age': 25},
# {'id': 1232, 'name': 123, 'age': 30},
# {'id': 7854, 'name': 'Bob', 'age': 22},
# {'id': 33412, 'name': None, 'age': 35},
# {'id': 78845, 'name': 'Charlie', 'age': 28},
# {'id': 45325, 'name': 'Eve', 'age': 40},
# {'id': 745633, 'name': True, 'age': 19},
# {'id': 64364, 'name': 'Frank', 'age': 33}
# ]
# Есть список пользователей users, где каждый пользователь представлен
# словарем с ключами id, name, и age. Некоторые пользователи могут иметь
#
# некорректное значение для ключа name. Под некорректным значением
# понимается любой тип, который не является строкой.
# - Создайте список ids, в который будут включены идентификаторы (id) тех
# пользователей, у которых значение по ключу name некорректно.
# - Выведите список на экран.
#
# Ответ должен быть: [1232, 33412, 745633]

users = [
{'id': 345324, 'name': 'Alice', 'age': 25},
{'id': 1232, 'name': 123, 'age': 30},
{'id': 7854, 'name': 'Bob', 'age': 22},
{'id': 33412, 'name': None, 'age': 35},
{'id': 78845, 'name': 'Charlie', 'age': 28},
{'id': 45325, 'name': 'Eve', 'age': 40},
{'id': 745633, 'name': True, 'age': 19},
{'id': 64364, 'name': 'Frank', 'age': 33}
]

ids = []
for user in users:
    if not isinstance(user['name'], str):
         ids.append(user['id'])
print(ids)