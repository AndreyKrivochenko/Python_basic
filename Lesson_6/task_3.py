class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_1 = Position('Иван', 'Петров', 'столяр', 15000, 3000)

print(vars(worker_1))
print(f'{worker_1.get_full_name()} получает {worker_1.get_total_income()} рублей')
