x = input('Input first number: ')
y = input('Input second number: ')

def name(x, y):
    if not(x.isdigit() and y.isdigit()):
        return 'you only need to enter numbers'

    x = int(x)
    y = int(y)
    

    if x > y:
        result = x - y
        return '%s > %s on ' %(x,y) + str(result) 
    elif x < y:
        result = y - x
        return '%s < %s on ' %(x,y)+str(result)
    elif x == y:
        return '%s = %s ' %(x,y)    



print(name(x, y))
