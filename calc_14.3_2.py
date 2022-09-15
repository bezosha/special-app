action = input('Выберите операцию: ')
count = int(input('Сколько операндов?: '))
full_str = ''
solution = 0
position = 1
while count != 0:
    if action == '+':
        operand = int(input('Введите операнд ' + str(position) + ': '))
        if count == 1:
            full_str += str(operand) + ' '
        else:
            full_str += str(operand) + ' ' + str(action) + ' '
        if position == 1:
            solution = operand
        else:    
            solution += operand
        position += 1
    elif action == '-':
        operand = int(input('Введите операнд ' + str(position) + ': '))
        if count == 1:
            full_str += str(operand) + ' '
        else:
            full_str += str(operand) + ' ' + str(action) + ' '
        if position == 1:
            solution = operand
        else:    
            solution -= operand
        position += 1
    elif action == '*':
        operand = int(input('Введите операнд ' + str(position) + ': '))
        if count == 1:
            full_str += str(operand) + ' '
        else:
            full_str += str(operand) + ' ' + str(action) + ' '
        if position == 1:
            solution = operand
        else:    
            solution *= operand
        position += 1
    elif action == '/':
        operand = int(input('Введите операнд ' + str(position) + ': '))
        if count == 1:
            full_str += str(operand) + ' '
        else:
            full_str += str(operand) + ' ' + str(action) + ' '
        if position == 1:
            solution = operand
        else:    
            solution /= operand
        position += 1
    else:
        print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
    count -= 1
print(full_str, '=', solution)