input_value = input('Enter value: \n')
b = ''
for i in input_value:
    if i == ',' or i == ' ':
        i = ''
    b += i
print(b)
