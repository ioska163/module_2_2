number1 = int(input("Введите 1 число:" ))
number2 = int(input("Введите 2 число:" ))
number3 = int(input("Введите 3 число:" ))
if  number1 == number2 == number3:
    print('3')
elif   number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print('0')