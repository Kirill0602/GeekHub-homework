'''
8. Створити цикл від 0 до ... (вводиться користувачем).
В циклі створити умову, яка буде виводити поточне значення,
якщо остача від ділення на 17 дорівнює 0.
'''

number = int(input('Enter number: \n'))
print('Current value whose remainder after division by 17 is 0:')
for i in range(0, number):
    if i%17 == 0:
        print(i)
