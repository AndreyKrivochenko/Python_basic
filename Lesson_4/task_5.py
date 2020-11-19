from functools import reduce


def calc_mult(a, b):
    return a * b


list_num = [num for num in range(100, 1001) if (num % 2) == 0]
print(reduce(calc_mult, list_num))
