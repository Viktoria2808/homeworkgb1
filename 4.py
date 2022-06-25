number = int(input('Введите целое положительное число: '))
chislo = number % 10 #для обозначения переменных?
number = number // 10 #для обозначения переменных?
while number > 0:
   if number % 10 > chislo:
       chislo = number % 10
   number = number // 10
print('Самая большая цифра числа: ', chislo)