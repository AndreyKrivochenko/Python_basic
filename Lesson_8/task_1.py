class DataValueError(Exception):
    pass


class Data:
    def __init__(self, data_string):
        self.data_string = data_string

    @classmethod
    def data_int(cls, data_string: str):
        return [int(data) for data in data_string.split('-')]

    @staticmethod
    def data_valid(data_list: list):
        if data_list[0] in range(1, 32) and data_list[1] in range(1, 13) and data_list[2] in range(0, 3000):
            print('Дата корректна')
        else:
            raise DataValueError(f'Некорректная дата - {data_list}')


data_1 = '31-08-2010'
try:
    Data.data_valid(Data.data_int(data_1))
except DataValueError as e:
    print(e)
