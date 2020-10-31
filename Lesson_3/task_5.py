def calc_number(*args):
    sum_num = 0
    for i in args:
        sum_num += i
    return sum_num


result = 0
flags = True
while flags:
    user_string = input('Введите числа через пробел, для выхода - q: ')
    user_list_str = user_string.split()
    user_list = []
    for val in user_list_str:
        if val == 'q':
            flags = False
        else:
            user_list.append(int(val))
    result += calc_number(*user_list)
    print(f'Промежуточная сумма = {result}')

print(f'Сумма = {result}')
