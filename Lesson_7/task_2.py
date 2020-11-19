from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, *args, **kwargs):
        self._area = None

    @abstractmethod
    def get_textile(self):
        return self._area

    def __str__(self):
        return f'{self.get_textile()}'

    def __add__(self, other):
        instance = self.__class__()
        instance._area = self.get_textile() + other.get_textile()
        return instance


class Coat(Clothes):
    def __init__(self, size=0):
        super().__init__()
        self.size = size

    def get_textile(self):
        if self._area is None:
            self._area = self.size/6.5 + 0.5
        return self._area


class Costume(Clothes):
    def __init__(self, height=0):
        super().__init__()
        self.height = height

    def get_textile(self):
        if self._area is None:
            self._area = 2 * self.height + 0.3
        return self._area

    @property
    def double_textile(self):
        return self.get_textile() * 2


coat_1 = Coat(38)
coat_2 = Coat(43)
print(coat_1)
costume_1 = Costume(190)
costume_2 = Costume(176)
print(costume_1)
total_textile = coat_1 + coat_2 + costume_1 + costume_2
print(total_textile)
print(f'1 - {costume_2}, 2 - {costume_2.double_textile}')
