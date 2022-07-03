from functools import reduce
def my_list(prev_el, now_el):
    return prev_el * now_el
my_list1 = [el for el in range(100, 1001, 2)]
print(f"Список\n{my_list1}\nУмножение списка\n{reduce(my_list, my_list1)}")

#Не получается сделать pull request
