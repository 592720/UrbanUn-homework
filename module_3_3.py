def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('1. Функция с параметрами по умолчанию:')
print_params()
print_params(a=54)
print_params(666)
#print_params(1, 2, 3, 4)
print_params('jk', 1111, False)
print_params(b = 25)
print_params(c = [1,2,3])
print('\n')

print('2. Распаковка параметров:')
values_list = ['OoO', 2.009, ('a', 'б', 'в')]
values_dict = {'a':-85, 'b':':3', 'c':[1, 258, 34]}
print_params(*values_list)
print_params(**values_dict)
print('\n')

print('3. Распаковка + отдельные параметры:')
values_list_2 = ['R', 5.5]
print_params(*values_list_2,42)