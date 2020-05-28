import json

with open('example/text_7.txt', 'r', encoding='utf-8') as f_cool:
    with open('text_77_2.json', 'w', encoding='utf-8') as g_cool:
        content_a = f_cool.readlines()
        content_b = dict()
        content_c = dict()
        sr_prib = []
        for stroka in content_a:
            a = stroka.split()
            if int(a[2]) - int(a[3]) > 0: sr_prib.append(int(a[2]) - int(a[3]))
            content_b[a[0]] = int(a[2]) - int(a[3])
        content_c['average.profit'] = sum(sr_prib) / len(sr_prib)
        sr_prib = [content_b, content_c]
        json.dump(sr_prib, g_cool)
