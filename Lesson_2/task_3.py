month = '12'
month = int(month)

# Поиск времени года через список. 1 вариант
# Ужас как громоздко, удалять не стал. Ниже придумал лучше

month_list = [
    [12, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]
month_list_index = None

for ind in range(len(month_list)):
    if month in month_list[ind]:
        month_list_index = ind

if month_list_index == 0:
    print('Зима')
elif month_list_index == 1:
    print('Весна')
elif month_list_index == 2:
    print('Лето')
else:
    print('Осень')

# Поиск времени года через список. 2 вариант
# Так немного лучше, но тоже как-то...

month_list = [1, 'Зима', 2, 'Зима', 3, "Весна", 4, 'Весна', 5, 'Весна', 6, 'Лето', 7, 'Лето',
              8, 'Лето', 9, 'Осень', 10, 'Осень', 11, 'Осень', 12, 'Зима']
month_list_index = month_list.index(month)
print(month_list[month_list_index+1])

# Поиск времени года через словарь
# Здесь вроде нагляднее получается

month_dict = {
    'Зима': (12, 1, 2),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}

for k, v in month_dict.items():
    if month in v:
        print(k)
