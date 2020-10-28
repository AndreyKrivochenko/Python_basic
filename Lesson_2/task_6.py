goods = []
count = int(input('Количество вводимых товаров? '))

for i in range(count):
    print(f'{i+1}-й Товар: ')
    name = input('Название: ')
    price = int(input('Цена: '))
    count_good = int(input('Количество: '))
    unit = input('Единица измерения: ')
    good_dict = {'название': name, 'цена': price, 'количество': count_good, 'ед': unit}
    good_tuple = tuple([i+1, good_dict])
    goods.append(good_tuple)

print(goods)

analytics_goods = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}

for g_dict in goods:
    for key, val in g_dict[1].items():
        analytics_goods[key].append(val)

for key, val in analytics_goods.items():
    analytics_goods[key] = list(set(val))

print(analytics_goods)
