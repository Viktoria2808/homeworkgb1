def myfunc(**kwargs):
    s = 0
    my_list = input('Введите числа: ').split()
    for i in my_list:
      if i == '#':
        return s, True
      try:
          s = int(i) + s
      except ValueError:
            pass
      return s, False


res = 0
while True:
    a, b = myfunc()
    res = a + res
    print(res)
    if b:
        break