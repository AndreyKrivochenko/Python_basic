class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Инструмент - {self.title}, рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Инструмент - {self.title}, рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Инструмент - {self.title}, рисуем маркером')


stat_1 = Pen('Ручка')
stat_1.draw()
stat_2 = Pencil('Карандаш')
stat_2.draw()
stat_3 = Handle('Маркер')
stat_3.draw()
