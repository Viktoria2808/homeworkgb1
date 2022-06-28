arg_1 = int(input('Введите первое число: '))
arg_2 = int(input(('Введите второе число: ')))
def my_func(arg_1, arg_2):
    return arg_1 // arg_2
if arg_2 == 0:
    print('На ноль делить нельзя')
else:
    print(my_func(arg_1, arg_2))
