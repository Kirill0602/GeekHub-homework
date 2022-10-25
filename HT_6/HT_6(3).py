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
class FirstException(Exception):
    pass
class SecondException(Exception):
    pass
class ThirdException(Exception):
    pass

def func():

    l = [['username1','password1'], ['username2', 'password2'], ['username3','password3'], ['username4','password'] ]


    for p in l:
        password = p[1]
        login = p[0]
        if 3 < len(login) > 50:
            raise FirstException('The username must be between 3 and 50 characters long!')
        if len(password) < 8:
            raise SecondException('Password contains less than 8 characters!')
        if len(password) > 16:
            raise ThirdException('Password is too long')
        for i in password:
            if i in '0123456789':
                print(f'Name: {login}\nPassword: {password}\nStatus: OK')
                break
        else:
            print(f'Name: {login}\nPassword: {password}\nStatus: Password must contain at least one number')
func()
