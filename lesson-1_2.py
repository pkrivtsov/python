sec = int(input('Введите время в секундах '))
hh = sec // 3600
mm = (sec - hh * 3600) // 60
sec = sec - mm * 60 - hh * 3600
time = str(hh) + ":" + str(mm) + ":" + str(sec)
print('Время в формате чч:мм:сс ' + time)
