'''
3. Користувач вводить змінні "x" та "y" з довільними цифровими значеннями. 
Створіть просту умовну конструкцію (звiсно вона повинна бути в тiлi ф-цiї), 
під час виконання якої буде перевірятися рівність змінних "x" та "y" та у випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y"
'''
x = input('Input first number: ')
y = input('Input second number: ')

def name(x, y):
    if not(x.isdigit() and y.isdigit()):
        return 'you only need to enter numbers'

    x = int(x)
    y = int(y)
    

    if x > y:
        result = x - y
        return '{} > {} on '.format(x,y) + str(result) 
    elif x < y:
        result = y - x
        return '{} < {} on '.format(x,y)+str(result)
    elif x == y:
        return '{} = {} '.format(x,y)    



print(name(x, y))
