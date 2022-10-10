#4. Write a script which accepts a <number> from user and then <number> times asks user for string input. 
#At the end script must print out result of concatenating all <number> strings.

number = int(input('Enter number: \n'))
for i in set(range(number + 1)):
    z = str(number)
    
print('Result of concatenating all: ', (z*i))    

