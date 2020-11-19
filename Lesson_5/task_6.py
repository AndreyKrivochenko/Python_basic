# Фунция очистки строки от символов
def del_not_number(string):
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_string = ''
    for sym in string:
        if sym in number_list:
            new_string = f'{new_string}{sym}'
    return int(new_string) if new_string else 0


with open('task_6.txt', 'r') as file:
    content = file.read().splitlines()

content = [string.split() for string in content]

result = {}
for item in content:
    result[item[0]] = sum(map(del_not_number, item[1:]))

print(result)
