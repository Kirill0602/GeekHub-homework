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


