with open('example/text_6.txt', 'r', encoding='utf-8') as f_cool:
    content_a = f_cool.readlines()
    content_b = dict()
    for stroka in content_a:
        a = stroka.split(':')
        h_d = 0
        for hour in a[1].split():
            for dis in hour.split('('):
                if dis.isdigit(): h_d += int(dis)
        content_b[a[0]] = h_d
    print(content_b)
