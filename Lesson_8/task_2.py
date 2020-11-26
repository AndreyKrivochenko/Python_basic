class ZeroDiv(Exception):
    pass


def user_division(a, b):
    if b == 0:
        raise ZeroDiv('На ноль делить нельзя')
    else:
        return a / b


try:
    print(user_division(5, 0))
except ZeroDiv as e:
    print(e)
