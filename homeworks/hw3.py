# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
# Распечатайте значения 1, 2, 3
def task1():
    my_list = ['a', 'b', [1, 2, 3], 'd']
    print(*my_list[2])


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
def task2():
    list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100, 10.5]
    print(sum([x for x in list_1 if type(x) in (int, float)]))
    print(*[s for s in list_1 if str(s).__contains__('a')])
    #print(*[s for s in list_1 if 'a' in str(s)])


# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
def task3():
    list_str = ['cat', 'dog', 'horse', 'cow']
    print(type(list_str))
    tuple_from_list = tuple(['cat', 'dog', 'horse', 'cow'])
    print(type(tuple_from_list))


# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом.
#      Если состав одинаковый, print("Equal')
def task4():
    family_1, family_2 = input().split(','), input().split(',')
    if len(family_1) > len(family_2):
        print('family_1')
    elif len(family_1) < len(family_2):
        print('family_2')
    else:
        print('Equal')


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor,
# slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
def task5():
    film = {'title': 'Title1',
            'director': 'Director1',
            'year': 1998,
            'budget': 1_000_000,
            'main_actor': 'Main Actor',
            'slogan': 'Slogan'
            }
    print(film.keys())
    print(film.values())
    print(film.items())


# 3.6. Найдите сумму всех значений в словаре
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
def task6():
    my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
    print(sum(my_dictionary.values()))


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
def task7():
    ls = [1, 2, 3, 4, 5, 3, 2, 1]
    print(ls)
    st = list(set(ls))
    print(st)


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'},
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
def task8():
    set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
    set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
    print(set1.intersection(set2))
    print(set1.symmetric_difference(set2))
    print((set1.issubset(set2)))
    print((set2.issubset(set1)))


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
task8()
