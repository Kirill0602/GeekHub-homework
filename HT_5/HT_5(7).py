'''
Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньому і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
'''
def func(lst):

    print('List: ', lst)
    lst1 = []

    for i in lst:
        if i not in lst1:
            lst1.append(i)
            b = lst.count(i)
            print(f'{i} repeats {b} times')
            
    return lst1
            


lst = 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]
print(func(lst))









