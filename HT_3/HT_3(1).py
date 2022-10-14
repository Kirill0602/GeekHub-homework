'''
1. Write a script that will run through a list of tuples and replace the last value for each tuple. 
The list of tuples can be hardcoded. The "replacement" value is entered by user.
The number of elements in the tuples must be different.
'''


list_of_tuple = [(1, 2, 3), ('abc', 'qwert'), ('y',), ()]
print('List of tuple: ', list_of_tuple)


change_value = input('Enter value: ')

data_storage = []
for i in list_of_tuple:
    li = list(i)
    li = li[:-1]
    li.append(change_value)
    li = tuple(li)
    data_storage += [li]
print('Change_value:',data_storage)


