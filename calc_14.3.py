action = input('Выберите операцию: ')
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
if action == '+':
    print (num_1,'+', num_2, '=', num_1 + num_2 )
elif action == '-':
    print (num_1,'-', num_2, '=', num_1 - num_2 )
elif action == '*':
    print (num_1,'*', num_2, '=', num_1 * num_2 )
elif action == '/':
    print (num_1,'/', num_2, '=', num_1 / num_2 )
else:
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')