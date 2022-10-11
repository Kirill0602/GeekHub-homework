#4. Write a script which accepts a <number> from user and then <number> times asks user for string input. 
#At the end script must print out result of concatenating all <number> strings.

result = []
cnt = int(input("Insert count:"))
for i in range(cnt):
    result.append(input())
print("Result:")
print(" ".join(result))
