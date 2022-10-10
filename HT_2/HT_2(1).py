#1. Write a script which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers.

enter_numbers = input('enter numbers: \n')
list = enter_numbers.split(',')
tuple = tuple(list)
print('List numbers: ', list)
print('Tuple numbers: ', tuple)
