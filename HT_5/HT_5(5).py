'''
5. Написати функцію <fibonacci>, яка приймає один аргумент
і виводить всі числа Фібоначчі, що не перевищують його.

'''
def fibonacci(number):
    b = 0
    c = 1
    while b <= number:
        print(b, end=' ')
        b, c = c, b + c
    return b-c

number = int(input('Input number: '))
print('Fibonacci numbers that do not exceed the entered number:')    
fibonacci(number)
