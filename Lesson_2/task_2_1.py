my_list = input('Введите элементы списка через пробел: ').split()

for val in range(0, len(my_list), 2):
    if val+1 < len(my_list):
        my_list[val], my_list[val+1] = my_list[val+1], my_list[val]
