#f = open(r'C:\\Program Files\doc.docx', 'r', encoding='utf-8') # режим чтения
#f = open('C:\\\\Program Files\\doc.docx', 'r', encoding='utf-8')
#f = open('C://Program Files/doc.docx', 'r', encoding='utf-8')
#f = open('doc.docx', 'r', encoding='utf-8')
#content = f.read() # читает от курсора до конца
#content = f.readline()#читает все с переводом
#content = f.readlines()#читает все с разбивом строк
#content = f.read().splitlines()
#content = f.read()# от курсора 2 симв
#print(content)
#f.close()#закрыть файл
for line in f:
    print(line, end='')
f.close()
f = open('doc2.docx', 'w', encoding='UTF-8') #открываем файл на запись
f.write(f"56, 78, 456 {[5, 7, 8]}")
f.write("Python\n")
f.writelines('Java\n', 'Hello\n')#записать список строк
print('C++',file=f)#указываем,  в какой файл надо писать(переменная)
print('Kotlin', file=f)
f.close()
with open('doc2.docx', 'w', encoding='UTF-8') as f:
