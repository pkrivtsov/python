d = {}
s1 = []
s2 = []
s3 = []
s4 = []
n = int(input('элементов в структуре: '))
for _ in range(n):
    s1.append(input('Введите наименование товара: '))
    s2.append(input('Введите цену соотвтетсвующего товара: '))
    s3.append(input('Введите количество: '))
    s4.append(input('Введите единицы, соотвтетсвующего товара: '))
d['название'] = s1
d['цена'] = s2
d['кол-во'] = s3
d['ед'] = s4
result = []
for i in range(1, n + 1):
    result.append((i, {k: v[i - 1] for k, v in d.items()}))
print(result)
