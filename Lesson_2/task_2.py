len_list = int(input('Введите длину списка: '))
my_list = []
for val in range(len_list):
    result = input(f'Введите {val}-й элемент: ')
    my_list.append(result)

# print(my_list)

for val in range(0, len(my_list), 2):
    if val+1 < len(my_list):
        my_list[val], my_list[val+1] = my_list[val+1], my_list[val]

# print(my_list)
