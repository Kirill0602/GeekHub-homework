'''
2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат 
(напр. інпут від юзера, результат математичної операції тощо). 
Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
обробляє їх результат та також повертає результат своєї роботи. 
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
'''
def launch_all():
    print('I am fourth function.')

    def func(enter):
        print('Output of the first function: {}'.format(enter))


    def sum_func(a, b):
        print('Output of the second function(sum of numbers): {}'.format(a + b))


    def multiplication_func(q, w):
        print('Output of the third function(multiplication of numbers 9*9): {}'.format(q*w))

        

    func(enter)
    sum_func(a, b)
    multiplication_func(9, 9)
    
enter = input('Write something: ')
a = int(input('input first number: '))
b = int(input('Input second number: '))


launch_all()
