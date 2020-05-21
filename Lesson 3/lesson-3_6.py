def int_func(slovo):
    return (slovo.title())


lst_text = input('Введите слова через пробел ').split()
for word in lst_text:
    valid = True
    for item in word:
        if 97 <= ord(item) <= 122:
            pass
        else:
            print(f'Слово {word} должно состоять из маленьких латинских букв')
            valid = False
            break
    if valid:
        print(int_func(word), end=' ')
