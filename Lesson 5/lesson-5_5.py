with open('text_5.txt', 'w', encoding='utf-8') as f_cool:
    num = [el for el in range(10)]
    print(sum(num))
    for i in num:
        f_cool.write(f'{i} ')
