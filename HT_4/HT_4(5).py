def calc(x, action, y):
    while True:
        if action == '+':
            print('%.2f + %.2f = %.2f' % (x, y, x+y))
        elif action == '-':
            print('%.2f - %.2f = %.2f' % (x, y, x-y))
        #elif action == '**':
            #print('%.2f ** %.2f = %.2f' % (x, y, x**y))
        elif action == '*':
            print('%.2f * %.2f = %.2f' % (x, y, x*y))
        #elif action == '//':
            #print('%.2f // %.2f = %.2f' % (x, y, x//y))
        elif action == '/':
            if y != 0:
                print('%.2f / %.2f = %.2f' % (x, y, x/y))
            else: 
                print("Division by zero!")

        break
        
try:
    x = float(input("Enter the first number: "))
    action = input("Action +, -, *, /: ")
    y = float(input("Enter the second number: "))
except ValueError:
    print("It's not a number")
try:
    calc(x, action, y)
except NameError:
    print('End program')
    



