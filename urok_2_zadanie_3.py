dict_month = {1:'zima',2: 'zima', 3:'vesna', 4: 'vesna', 5: 'vesna', 6: 'leto', 7: 'leto', 8: 'leto', 9: 'osen', 10: 'osen', 11: 'osen', 12: 'zima' }
list_month = ['zima', 'zima', 'vesna', 'vesna', 'vesna', 'leto', 'leto', 'leto', 'osen', 'osen', 'osen', 'zima']
month = int(input('Введите месяц в виде целого числа: '))
if month in dict_month:
    print(list_month[month-1]) #так как январь должен быть не 0, а 1
    print(dict_month[month])