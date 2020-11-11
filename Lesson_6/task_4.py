class Car:
    def __init__(self, name, color, is_police=False):
        self.speed = None
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if speed <= 0:
            print('Для движения нужна положительная скорость больше ноля')
        elif speed == self.speed:
            print(f'Уже двигаемся {self.speed} км/ч')
        else:
            self.speed = speed
            print(f'Поехали {self.speed} км/ч')

    def stop(self):
        if not self.speed:
            print('Уже стоим')
        else:
            self.speed = None
            print('Остановились')

    def turn(self, direction):
        if not self.speed:
            print('Для поворота нужно двигаться, сейчас мы стоим')
        elif direction == 'left':
            print('Повернули налево')
        elif direction == 'right':
            print('Повернули направо')

    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч')
        if self.speed > 60:
            print('Вы превышаете')


class WorkCar(Car):
    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч')
        if self.speed > 40:
            print('Вы превышаете')


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, is_police=True)


class SportCar(Car):
    def __init__(self, name, color, is_police, volume_engine):
        super().__init__(name, color, is_police)
        self.volume_engine = volume_engine


car_1 = WorkCar('Toyota', 'white')
car_1.stop()
car_1.go(20)
car_1.go(20)
car_1.stop()
car_1.stop()
car_1.turn('left')
car_1.go(50)
car_1.turn('left')
car_1.show_speed()

car_2 = PoliceCar('Corvette', 'black')
print(vars(car_2))
print(vars(car_1))
sport_car = SportCar('Porsche', 'red', False, '5.5L')
print(vars(sport_car))
