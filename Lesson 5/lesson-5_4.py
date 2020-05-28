with open('example/text_4.txt', 'r', encoding='utf-8') as f_cool:
    with open('text_4_2.txt', 'w', encoding='utf-8') as g_cool:
        content_a = f_cool.readlines()
        content_b = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
        result = []
        for stroka in content_a:
            a = stroka.split('-')
            result.append(' - '.join((content_b.get(a[0].strip()) or a[0].strip(), a[1].strip())))
        for item in result:
            g_cool.write(f'{item}\n')
