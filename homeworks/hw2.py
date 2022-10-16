# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
#
def check_health():
    health = int(input('Введите уровень здоровья вашего персонажа: '))
    print(health >= 0)


# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
#
def is_even():
    number = int(input('Введите любое число: '))
    print('Чётное' if number % 2 else 'Нечётное')


# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400,
# он также считается високосным (1200, 2000)
#
def is_leap():
    year = int(input())
    print('Високосный' if not year % 4 and year % 100 or not year % 400 else 'Невисокосный')


# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз,
# построчно. Текст и количество повторений нужно ввести с помощью input()

def print_text():
    text = input('Введите текст: ')
    count = int(input('Введите количество повторений: '))
    for _ in range(count):
        print(text)


# check_health()
# is_even()
# is_leap()
# print_text()