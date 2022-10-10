#3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input("Enter number: \n"))
result = sum(range(number + 1))
print("Sum of the first", number ,"positive integers:",result)
