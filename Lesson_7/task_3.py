class Unit:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'{self.count}'

    def __add__(self, other):
        return Unit(self.count + other.count)

    def __sub__(self, other):
        if self.count >= other.count:
            result = Unit(self.count - other.count)
        else:
            raise ValueError('Вычитаемое больше уменьшаемого')
        return result

    def __mul__(self, other):
        return Unit(self.count * other.count)

    def __truediv__(self, other):
        return Unit(int(self.count / other.count))

    def make_order(self, cells):
        cells_list = []
        count = self.count
        for i in range(int(self.count / cells) + 1):
            if count > cells:
                cells_list.append(f'{"*" * cells}\n')
            else:
                cells_list.append(f'{"*" * count}\n')
            count -= cells
        return ''.join(cells_list)


a1 = Unit(10)
a2 = Unit(5)
a3 = Unit(7)
a4 = a1 + a2 + a3
print(a4)

try:
    a5 = a1 - a2 - a3
    print(a5)
except ValueError as e:
    print(f'Ошибка вычитания: {e}')

a6 = a1 * a2 * a3
print(a6)

a7 = a6 / a4 / a3
print(a7)
print(a4.make_order(6))
