def my_func_1(x, y):
    x = float(x)
    y = int(y)
    return x ** y


def my_func_2(x, y):
    x = float(x)
    y = int(y)
    result = x
    for i in range(abs(y)-1):
        result *= x
    return 1 / result


print(my_func_1(35.6, -3))
print(my_func_2(35.6, -3))
