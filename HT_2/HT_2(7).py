#7. Write a script to concatenate all elements in a list into a string and print it. 
#List must include both strings and integers and must be hardcoded.

input_value = input('Enter value: \n')
b = ''
for i in input_value:
    if i == ',' or i == ' ':
        i = ''
    b += i
print(b)
