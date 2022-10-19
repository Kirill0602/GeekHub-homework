'''
3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні.
'''

def is_prime(number):
    
    if number <= 1000:
        for i in range(2, (number//2)+1):
            if number % i == 0:
                print(f'{number} Is not a prime number')
                return False
        print(f'{number} Prime number')
        return True
    else:
        print('Input number is greater than 1000')
    
number = int(input('Input number from 1 to 1000: '))
print(is_prime(number))
