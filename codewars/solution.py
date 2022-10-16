# import math
#
# import numpy as np
#
#
# def are_you_playing_banjo(name):
#     if name[0] in "rR":
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
#
#
# # Clock shows h hours, m minutes and s seconds after midnight.
# # Your task is to write a function which returns the time since
# # midnight in milliseconds.
# def past(h, m, s):
#     return (60 * 60 * h + 60 * m + s) * 1000


# def find_average(numbers: []):
#     count = 0
#     total = 0
#     for i in numbers:
#         total += i
#         count += 1
#     return int(total / count)

# def find_average(numbers: []):
#     return int(np.average(numbers))



def fizz_buzz():
    for i in range(1, 21):
        if not i % 3 and not i % 5:
            print('FizzBuzz')
        elif not i % 3:
            print('Fizz')
        elif not i % 5:
            print('Bizz')
        else:
            print(i)


def fibo(num):
    f0 = 0
    f1 = 1
    print(f0)
    print(f1)
    for i in range(0, num + 1):
        fib = f0 + f1
        f0 = f1
        f1 = fib
        print(fib)


fibo(10)
# fizz_buzz()
# print(find_average([1, 2, 3]))
# print('123 456 789'.isalnum())
