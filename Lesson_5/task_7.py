import json

with open('task_7.txt', 'r') as file:
    content = file.readlines()
    content = [string.rstrip() for string in content]

# Заполняем словарь с прибылью фирм
result_profit = {}
for item in content:
    list_string = item.split()
    profit = int(list_string[2]) - int(list_string[3])
    result_profit[list_string[0]] = profit

# Считаем среднюю прибыль по фирмам с положительной прибылью
average_profit = 0
profit_firm = 0
for val in result_profit.values():
    if val > 0:
        average_profit += val
        profit_firm += 1
average_profit /= profit_firm

# Создаем словарь со средней прибылью
average = {'average_profit': average_profit}

# Результирующий список из словарей
result = [result_profit, average]

# Записываем список в json-файл
with open('task_7.json', 'w') as file:
    json.dump(result, file)
