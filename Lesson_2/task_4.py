# user_string = input('Введите строку: ')
user_string = 'привет мой капитализированный друг'

string_list = user_string.split()

for num in range(len(string_list)):
    print(f'{num}) {string_list[num][:10]}')
