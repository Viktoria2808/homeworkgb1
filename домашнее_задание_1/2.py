time = int(input('Введите время в секундах: '))
hour = time / 3600
print(hour)
min = time / 60
print(min)
sek = time
print(sek)
print('{0}; {1}; {2};'.format(hour, min, sek))
print('{}'.format([hour, min, sek]))
time = '%d:%d:%d'% (hour, min, sek)
print(time)