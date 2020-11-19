month = '2'
month = int(month)
season = ['Зима', 'Весна', 'Лето', 'Осень']

if month in range(1, 13):
    print(season[month // 3 % 4])
else:
    print('Вы ввели неверное число')
