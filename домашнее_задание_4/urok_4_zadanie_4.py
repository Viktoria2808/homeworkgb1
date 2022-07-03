my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
d = {}
for i in my_list:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
new_list = [el for el in my_list if d[el] == 1]
print(new_list)
