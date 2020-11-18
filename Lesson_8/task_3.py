class OnlyDigit(Exception):
    pass


class Digit:
    def __init__(self, data):
        self.data = data

    def control(self):
        try:
            float(self.data)
        except ValueError:
            raise OnlyDigit('Необходимо число')


digit_list = []
digit = input('Введите число, для выхода введите "stop": ')
while digit != 'stop':
    digit = Digit(digit)
    try:
        digit.control()
        digit_list.append(float(digit.data))
    except OnlyDigit as e:
        print(f'OnlyDigit: {e}')
    digit = input('Введите число, для выхода наберите "stop": ')

print(digit_list)
