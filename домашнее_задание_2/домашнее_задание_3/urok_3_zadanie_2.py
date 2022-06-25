def my_param(**kwargs):
    return ','.join(kwargs.values())
print(my_param(name=input('Enter your name'),
               surname=input('Enter your surname'),
               year_of_birth=(input('Enter your date of birth:')), mail=input('Enter your mail:'),
               city=input('Enter your city'), phone=input('Enter your phone num: ')))