my_list = [18, 3.14, 'String', False, [1, 2, 2], ('one', 'two'), {35, 18}, None]

for type_el in my_list:
    print(f'{str(type_el):>15} - type {type(type_el)}')
