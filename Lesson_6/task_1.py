from datetime import datetime, timedelta


class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зелёный']

    def running(self):
        def timer(second):
            time_now = datetime.now()
            time_next = time_now + timedelta(seconds=second)
            while time_now <= time_next:
                time_now = datetime.now()

        for i in range(3):
            print(self.__color[i])
            if i == 0:
                timer(7)
            elif i == 1:
                timer(2)
            else:
                timer(7)


tl_1 = TrafficLight()
tl_1.running()
