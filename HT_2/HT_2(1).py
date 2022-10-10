#1. Write a script which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers.

enter_numbers = input('enter numbers: \n')

list_numbers = [enter_numbers]
print('List numbers: ')
print(list_numbers)

tuple_numbers = tuple(list_numbers)
print('Tuple numbers: ')
print(tuple_numbers)
