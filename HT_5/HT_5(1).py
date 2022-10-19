'''
1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, 
і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.
'''
def square():

    side_of_square = float(input('Input side of square: '))
    perimeter_square = side_of_square * 4
    area_of_square = side_of_square * side_of_square
    diagonal_square = side_of_square * (2 ** 0.5)
    result = (perimeter_square, area_of_square, diagonal_square)
    print(f'Perimetr: {perimeter_square} \nArea: {area_of_square} \nDiagonal: {diagonal_square}')
    return result

square()



