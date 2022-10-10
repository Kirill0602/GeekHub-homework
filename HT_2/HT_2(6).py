#6. Write a script to check whether a value from user input is contained in a group of values.

input_value = input('Input your first values: \n')
group_value = input('Input your second values: \n')

if input_value == group_value:
    print('Input value match: True')
else:
    print('Input value mismatch in a group of values: False')





"""
2 variant

def checking_values(group_value, number_value):    
    return number_value in group_value


input_value = input('input your first values: \n')
group_value =input('input your second values: \n')
print(checking_values(input_value, group_value))
"""



