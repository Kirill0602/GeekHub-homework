'''
3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''
def func():

    l = [['username1','password1'], ['username2', 'password2'], ['username3','password3'], ['username4','password'] ]


    for p in l:
        password = p[1]
        login = p[0]
        if 3 < len(login) > 50:
            try:
                raise 'The username must be between 3 and 50 characters long!'
            except TypeError:
                print('The username must be between 3 and 50 characters long!')
        if len(password) < 8:
            try:
                raise 'Password contains less than 8 characters!'
            except TypeError:
                print('Password contains less than 8 characters!')
        if len(password) > 16:
            try:
                raise 'Password is too long'
            except TypeError:
                print('Password is too long')
        for i in password:
            if i in '0123456789':
                print(f'Name: {login}\nPassword: {password}\nStatus: OK')
                break
        else:
            try:
                raise 'Password must contain at least one number'
            except TypeError:
                print(f'Name: {login}\nPassword: {password}\nStatus: Password must contain at least one number')
func()
