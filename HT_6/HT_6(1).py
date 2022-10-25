'''
1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException (його також треба створити =))
'''

class LoginException(Exception):
    pass

def login_pass(username, password, silent=False):
    users = {'username1': 'password1',
             'username2': 'password2',
             'username3': 'password3',
             'username4': 'password5',
             'username5': 'password5'}

    variable = users.get(username, False) == password
    if not variable and not silent:
        try:
            raise LoginException
        except LoginException:
            print('LoginException')
    return variable

print(login_pass('username1', 'password1'))
print(login_pass('username2', 'password3'))
print(login_pass('username2', 'password3', silent=True))


