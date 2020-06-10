#  -------------------------------------------------------- 1 ----------------------------------------------------------


with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        # file.write(line + '\n')
        print(line, file=f)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_file = open("text_1.txt", 'w', encoding='utf-8')

line = None
while line != '':
    line = input("пишите или не пишите!: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()

#  -------------------------------------------------------- 2 ----------------------------------------------------------


counter = 0
with open("text_2.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split()
        print(line, 'Длина строки: ', len(line_words))
    print('Всего строк: ', counter)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open("text_2.txt", encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        number_of_words = len(value.split())
        print(f'Строка {index} содержит {number_of_words} слов')

#  -------------------------------------------------------- 3 ----------------------------------------------------------


with open("text_3.txt", "r", encoding="utf-8") as my_file:
    s_sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])

print(f"Salary less 20 000 {less}. Average salary - {sum(map(float, s_sum)) / len(s_sum)}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


def task_3():
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают:')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
    except:
        print('Что-то пошло не так')


task_3()
print('Итого как всегда меньше всех работал и больше всех получает )))')

#  -------------------------------------------------------- 4 ----------------------------------------------------------


rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "a") as new_file:
    with open("text_4.txt") as my_file:
        line = my_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(rus_dic[i[0]] + ' - ' + i[1] + "\n")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from googletrans import Translator

with open("text_4_translate.txt", 'w', encoding='utf-8') as f:
    with open("text_4.txt", 'r', encoding='utf-8') as f1:
        text = f1.read()
    f.write(Translator().translate(text, dest='ru').text)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import requests
import json

"""Переводит с английского на русский файл, результат записывается в новый файл.
Должен быть установлен модуль requests.
"""
token = "trnsl.1.1.20200416T132512Z.0bdb58c00f70557b.b1aec4ed1dc72e76cc6c08980f7ed0c2de92ae86"
url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

with open("task_4_text_yandex.txt", "w", encoding="utf-8") as f_result:
    with open("text_4.txt", encoding="utf-8") as f_4:
        for line in f_4:
            eng_text = line
            trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans, params=trans_option)
            trans_dict = json.loads(webRequest.text)
            line_to_result = "".join(trans_dict["text"])
            f_result.write(line_to_result)

print(f"Text translate from {f_4.name} has been done in {f_result.name}")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


from random import randint

sum_el = 0
with open("text.txt", "w", encoding="utf-8") as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file.write(str(el) + " ")

print(f"Sum of elements - {sum_el}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from random import randint

num_str = " ".join([str(randint(1, 1000)) for _ in range(100000)])
with open('task_5_file.txt',  mode='w+', encoding='utf-8') as the_file:
    the_file.write(num_str)
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))

#  -------------------------------------------------------- 6 ----------------------------------------------------------


mydict = {}
with open("text_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        mydict[name] = name_sum
print(f"{mydict}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open('text_6.txt', 'r', encoding='utf8') as text_file:
    a = text_file.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open('text_6.txt', encoding='utf8') as file:
    my_dict = dict()
    for line in file:
        name, other = line.split(": ")
        for i in other.split():
            if i != "-":
                my_dict[name] = my_dict.get(name, 0) + int(i.split("(")[0])

    print(my_dict)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


result = {}
with open("text_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        lesson_timing = []
        lessons = ([el for el in line.split(" ")])
        for el in lessons:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(result)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import re

subs_total_hours = {}

with open("text_6.txt") as f:
    for line in f.readlines():
        subs_total_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(subs_total_hours)

#  -------------------------------------------------------- 7 ----------------------------------------------------------


import json

result = []
with open("my_ex7.json", "w", encoding="utf-8") as write_f:
    with open("text_7.txt", encoding="utf-8") as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({"average_profit": round(average_profit)})
    json.dump(result, write_f)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import json

with open("text_77.json", "w", encoding='utf-8') as j_file:
    with open('text_7.txt', encoding='utf-8') as my_file:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = my_file.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["average_profit"] = k / o
        all_list = [subjects, middle]
    json.dump(all_list, j_file, ensure_ascii=False, indent=4)

print(f"All information on firms:\n{line}\n\nTotal list:\n{all_list}")
