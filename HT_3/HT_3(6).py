'''
6. Write a script to get the maximum and minimum VALUE in a dictionary.
'''

students = {
  'Anatoly': 25.6,
  'Kyrylo': '30',
  'Gregory': 20,
  'Sergey': 29.35, 
}

print('Dictionary:', students)
p = input('Do you want to know the maximum and minimum values of dictionaries?\nPress Enter \n')

my_list = []
for i in students.values():
    if type(i) == int or type(i) == float:
        my_list.append(i)
        
if p == '':
    print('Maximum value in a dictionary:',max(my_list))
    print('Minimum value in a dictionary:',min(my_list))
else:
    print('Goodbye')
