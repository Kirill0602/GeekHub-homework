'''
6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто функція приймає два аргументи: список і величину зсуву
(якщо ця величина додатна - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''
def cyclic_shift(fnc, shift):
    
    if shift < 0:
        shift = abs(shift)
        for i in range(shift):
            fnc.append(fnc.pop(0))
    else:
        for i in range(shift):
            fnc.insert(0, fnc.pop())
            
    return fnc

fnc = [1, 2, 3, 4, 5]
print('List: ', fnc)
shift = int(input('Enter number for the shift: '))
print('Result: ', cyclic_shift(fnc, shift))
            

            
