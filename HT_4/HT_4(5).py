'''
5. Ну і традиційно - калькулятор 🙂 Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя, яку зробити! 
Аргументи брати від юзера (можна по одному - окремо 2, окремо +, окремо 2; можна всі разом - типу 2 + 2). 
Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок!
'''
def calc(x, action, y):
    while True:
        if action == '+':
            print('{} + {} = {}'.format(x, y, x+y))
        elif action == '-':
            print('{} - {} = {}'.format(x, y, x-y))
        elif action == '**':
            print('{} ** {} = {}'.format(x, y, x**y))
        elif action == '*':
            print('{} * {} = {}'.format(x, y, x*y))
        elif action == '//':
            print('{} // {} = {}'.format(x, y, x//y))
        elif action == '%':
            print('{} % {} = {}'.format(x, y, x%y))
        elif action == '/':
            if y != 0:
                print('{} / {} = {}'.format(x, y, x/y))
            else: 
                print("Division by zero!")

        break
        
try:
    
    x = float(input("Enter the first number: "))
    action = input("Action +, -, *, **, /, //, % : ")
    y = float(input("Enter the second number: "))
    calc(x, action, y)
except ValueError:
    print("It's not a number")


