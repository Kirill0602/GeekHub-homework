'''
6. Write a script to get the maximum and minimum VALUE in a dictionary.
'''

students = {
  'Anatoly': 25,
  'Kyrylo': 30,
  'Gregory': 20,
  'Sergey': 29, 
}

print('Dictionary:', students)
p = input('Do you want to know the maximum and minimum values of dictionaries?\nPress Enter \n')
if p == '':
    print('Maximum value in a dictionary:',max(students.values()))
    print('Minimum value in a dictionary:',min(students.values()))
else:
    print('Goodbye')
