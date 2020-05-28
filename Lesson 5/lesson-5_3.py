with open('example/text_3.txt', 'r', encoding='utf-8') as f_cool:
    content = f_cool.readlines()
    sum = 0
    for stroka in content:
        if float(stroka.split()[1]) < 20000: print(stroka.split()[0], end=' ')
        sum += float(stroka.split()[1])
    print(f'\nСредний оклад: {sum / len(content)}')
