'''
4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення.
'''
def prime_list(start_of_range, end_of_range):
    
    if not(start_of_range.isdigit() and end_of_range.isdigit()):
        return 'You only need to enter numbers!'
    elif start_of_range.isdigit() and end_of_range.isdigit():
        start_of_range = int(start_of_range)
        end_of_range = int(end_of_range)
        
    l = []
    
    for x in range(start_of_range, end_of_range):
        d = 2
        while x % d != 0:
            d += 1
        if d == x:
            l.append(x)
    print('list of primes in your range: ')

    return l

start_of_range = input('Enter a number from which to start searching for natural numbers: ')
end_of_range = input('Enter the number to which natural numbers will be searched: ')

print(prime_list(start_of_range, end_of_range))
