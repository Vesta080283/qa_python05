import math
from functools import reduce
import my_calc


# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
def task1(side: float):
    perimetr = side * 4
    square = side ** 2
    diagonal = math.sqrt(math.pow(side, 2) * 2)
    return (perimetr, square, diagonal)


# 4.2. Напишите фукнцию, которая принимает произвольное
# количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
def task2_1(**kwargs):
    for key in kwargs.keys():
        print(f'{key}:{kwargs[key]}')


def task2_2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только  положительные числа
def task3():
    my_list = [20, -3, 15, 2, -1, -21]
    return list(filter(lambda x: x > 0, my_list))


# 4.4. Используя лямбда выражение, получите результат перемножения значений
# в предыдущем списке
def task4():
    my_list = [20, -3, 15, 2, -1, -21]
    return reduce(lambda x, y: x * y, my_list)






















# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции,
# выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.
def task5():
    prod_res = my_calc.prod(100, 20)
    print(prod_res)

    div_res1 = my_calc.divide(45, 9)
    print(div_res1)

    div_res2 = my_calc.divide(5, 0)
    print(div_res2)

    add_res = my_calc.add(585, 1987)
    print(add_res)

    remain_res = my_calc.remain(541, 6)
    print(remain_res)

    sub_res = my_calc.subtract(230, 149)
    print(sub_res)


def tests():
    assert my_calc.add(5, 8) == 13, f'Wrong number, actual result is {5 + 8}'
    assert my_calc.prod(10, 6) == 60, f'Wrong number, actual result is {10 * 6}'
    assert my_calc.divide(10, 0) == "Can't divide by zero", "Shouldn't divide by zero"
    assert my_calc.subtract(85, 28) == 57, f'Wrong number, actual result is {85 - 28}'
    assert my_calc.remain(9, 4) == 1, f'Wrong number, actual result is {9 % 4}'


print(task1(5))
print(task2_1(name='John', last_name='Smith', age=35, position='Developer'))
print(task2_2(name='John', last_name='Smith', age=35, position='Developer'))
print(task3())
print(task4())
task5()
tests()
