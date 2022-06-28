new_task = input('Введите строку: ').split()
for word in range(len(new_task)):
    if len(new_task[word]) <= 10:
        print(word, new_task[word])
    else:
         print(word, new_task[word][:10])


#
