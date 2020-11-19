revenue = 2364   # Выручка
costs = 1000     # Расходы
count = 16        # Количество сотрудников

if revenue > costs:
    print(f'Вы работаете с прибылью, рентабельность выручки = {(revenue - costs) / revenue:.2f}')
    print(f'Прибыль фирмы в расчете на одного сотрудника = {(revenue - costs) / count:.2f}')
elif revenue < costs:
    print('Вы работаете в убыток')
else:
    print('Ваши расходы равны выручке')
