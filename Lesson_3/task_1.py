def div_num(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        result = 'Нельзя делить на 0'
    return result


number_1 = 35
number_2 = 126

print(div_num(number_1, number_2))
