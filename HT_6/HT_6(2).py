'''
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило (smiley)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.

'''
def func(login, password):
    if 3 < len(login) > 50:
        raise 'The username must be between 3 and 50 characters long!'
    if len(password) < 8:
        raise 'Password contains less than 8 characters!'
    if len(password) > 16:
        raise 'Password is too long'
    for i in password:
        if i in '0123456789':
            break
    else:
        raise 'Password must contain at least one number'

    
    return login, password
    
print(func('Username', 'aaaaaaa1'))

