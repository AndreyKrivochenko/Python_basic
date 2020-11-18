class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}{self.b:+}\033[3mj'

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNum(a, b)

    def __mul__(self, other):
        a_1 = self.a * other.a
        a_2 = self.b * other.a
        b_1 = self.a * other.b
        b_2 = -(self.b * other.b)
        a = a_1 + b_2
        b = a_2 + b_1
        return ComplexNum(a, b)


num_1 = ComplexNum(1, -2)
print(num_1)
num_2 = ComplexNum(3, 4)
print(num_2)
num_3 = num_1 + num_2 + num_2
print(num_3)
num_4 = num_1 * num_2 * num_3
print(num_4)
