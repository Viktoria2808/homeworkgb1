my_list = [7, 5, 3, 3, 2]
reit = int(input('Введите новый элемент рейтинга: '))
i = 0  #индекс элемента равен нулю
for c in my_list: # с- каждый элемент в списке
    if reit <= c:
        i = i + 1 # или i+=1
my_list.insert(i, reit) # insert позволяет поставить элемент по индексу
print(my_list)

