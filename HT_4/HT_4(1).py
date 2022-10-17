'''
1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року,
до якої цей мiсяць належить (зима, весна, лiто або осiнь). 
У випадку некоректного введеного значення - виводити відповідне повідомлення.
'''
number_month = input('Enter the number of the month from 1 to 12: ')

def season(number_month):
    
    winter = 12, 1, 2
    spring = 3, 4, 5
    summer = 6, 7, 8
    autumn = 9, 10, 11

    if not number_month.isdigit():
        return 'Invalid Entry'

    number_month = int(number_month)

    if number_month in winter:
        return 'Month is winter'

    elif number_month in spring:
        return 'Month is spring'
    
    elif number_month in summer:
        return 'Month is summer'

    elif number_month in autumn:
        return 'Month is autumn'
    else:
        return 'Number entered is invalid'
        
print(number_month, season(number_month))
    
