class NotInWare(Exception):
    pass

class OfficeEquipment:
    def __init__(self, manufacturer, model, *args):
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self):
        if self.__class__ == Printer:
            vid = 'Printer'
        elif self.__class__ == Scanner:
            vid = 'Scanner'
        else:
            vid = 'Copier'
        return f'{vid} {self.manufacturer} {self.model}'


class Warehouse:
    ware = {
        'Printer': [],
        'Scanner': [],
        'Copier': []
        }

    @classmethod
    def append_item(cls, item: OfficeEquipment, count):
        if type(count) != int or count <= 0:
            print('Количество должно быть целым положительным числом')
        else:
            cls.ware[str(item.__class__.__name__)].append([item, count])

    @classmethod
    def del_item(cls, item: OfficeEquipment, count):
        index_item = None
        for i, val in enumerate(cls.ware[str(item.__class__.__name__)]):
            if val[0] == item:
                index_item = i
        if index_item is not None:
            if cls.ware[str(item.__class__.__name__)][index_item][1] > count:
                cls.ware[str(item.__class__.__name__)][index_item][1] -= count
            elif cls.ware[str(item.__class__.__name__)][index_item][1] == count:
                del cls.ware[str(item.__class__.__name__)][index_item]
            else:
                print(f'Товара {str(item)} на складе недостаточно')
        else:
            raise NotInWare('Товар отсутствует на складе')


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, print_type):
        super().__init__(manufacturer, model)
        self.print_type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, resolution):
        super().__init__(manufacturer, model)
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, model, speed):
        super().__init__(manufacturer, model)
        self.speed = speed


printer_1 = Printer('Epson', 'R300', 'Ink')
printer_2 = Printer('HP', 'LaserJet 1010', 'Laser')
scanner_1 = Scanner('Epson', 'Perfection V19', 4800)
scanner_2 = Scanner('Epson', 'Perfection V550', 9600)
copier_1 = Copier('Xerox', 'WorkCentre 5020', 20)
copier_2 = Copier('Xerox', 'WorkCentre 5016', 18)

Warehouse.append_item(copier_1, 2)
Warehouse.append_item(printer_1, 1)
Warehouse.append_item(printer_2, 3)
Warehouse.append_item(scanner_1, 1)
Warehouse.append_item(scanner_2, 2)
Warehouse.append_item(copier_2, '1')

for item in Warehouse.ware:
    for val in Warehouse.ware[item]:
        print(f'{val[0]}, {val[1]} шт.')
try:
    Warehouse.del_item(copier_2, 1)
except NotInWare as e:
    print(f'Ошибка удаления - {e}')
