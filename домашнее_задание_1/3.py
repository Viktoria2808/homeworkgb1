number = int(input('Введите число: '))
sum = 0
while (number != 0):
    posl = number % 10
    sum = sum + posl
    number = number // 10
print('Сумма чисел равна: ', sum)

