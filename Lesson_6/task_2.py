class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_1m_on_1sm, count_sm):
        return self._length * self._width * mass_1m_on_1sm * count_sm


road_1 = Road(5000, 20)
print(road_1.calc_mass(25, 5))