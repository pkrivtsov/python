class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


number = []
keep = True

while keep:

    for i in input('Числа через пробел или stop - завершить: ').split():
        try:
            if i == 'stop':
                keep = False
                break
            elif not i.isdigit():
                raise OwnError('not a number.')
            number.append(int(i))

        except OwnError as err:
            print(f'Value {i} {err}')

print(number)
