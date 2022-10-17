'''
2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат 
(напр. інпут від юзера, результат математичної операції тощо). 
Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
обробляє їх результат та також повертає результат своєї роботи. 
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
'''
def func(enter):
    print(f'Output of the first function: {enter}')
    return enter

def sum_func(a, b):
    result = a + b
    result1 = f'Output of the first function: {result}'
    print(result1)
    return result1


def multiplication_func(q, w):
    print(f'Output of the third function(multiplication of numbers 9*9): {q * w}')
    return q * w

        
def launch_all():
    print('I am fourth function.')
    func(enter)
    sum_func(a, b)
    multiplication_func(9, 9)
    return 
    
enter = input('Write something: ')
a = int(input('input first number: '))
b = int(input('Input second number: '))



launch_all()

