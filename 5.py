vyrochka = int(input('Введите значение выручки: '))
izderzhki = int(input('Введите значение издержек: '))
sotrudniki = int(input('Введите количество сотрудников: '))
pribil = vyrochka - izderzhki
ubitok = izderzhki - vyrochka
rent = pribil / vyrochka
result = pribil / sotrudniki
if (vyrochka > izderzhki):
    pribil = vyrochka - izderzhki
    print('прибыль равна: ', pribil)
    rent = pribil / vyrochka
    print('рентабельность равна: ',rent )
    result = pribil / sotrudniki
    print('Прибыль на сотрудника равна: ', result)
elif (vyrochka < izderzhki):
    ubitok = izderzhki - vyrochka
    print('убыток равен: ', ubitok)
else:
    print('Прибыль равна нулю')

