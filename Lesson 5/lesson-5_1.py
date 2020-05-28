with open('text.txt', 'a', encoding='utf-8') as f_cool:
    text = ' '
    while text != '':
        text = input('Введите текст или нажмите Enter для завершения: ')
        print(text, file=f_cool)
