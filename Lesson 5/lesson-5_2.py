with open('text.txt', 'r', encoding='utf-8') as f_cool:
    content = f_cool.readlines()
    print(f'Всего строк: {len(content)}')
    for idx, stroka in enumerate(content):
        print(f'В {idx + 1}-й строке, {len(stroka.split())} слов(а)')
