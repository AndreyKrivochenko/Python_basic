from sys import argv


def calc_salary(*args):
    result = int(args[0]) * int(args[1])
    if len(args) > 2:
        result += int(args[2])
    return result


param = argv[1:]
if len(param) > 1:
    print(calc_salary(*param))
