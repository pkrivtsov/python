class Data:
    def __init__(self, *args):
        self.param = args

    @classmethod
    def my_data(cls, param):
        result = []
        for item in param.split('-'):
            result.append(int(item))

        return Data(*result)

    @staticmethod
    def valid(*args):
        day, month, year = args
        if 1 < day < 31 and 1 < month < 12 and 1900 < year < 9999:
            return True
        return False


dt = Data.my_data('45-12-2020')
print(dt.valid(*dt.param))
