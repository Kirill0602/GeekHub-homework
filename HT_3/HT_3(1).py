print('Your list of tuples: ', [(1, 2, 3, 5), (3, 2, 4), (5, 6)])

list_of_tuples = list([(1, 2, 3, 5), (3, 2, 4), (5, 6)])

for i in range(len(list_of_tuples)):
    input1 = int(input('Enter first number and press Enter: '))
    tuple1_in_list = list(list_of_tuples[0])
    tuple1_in_list[3] = input1
    input2 = int(input('Enter second number and press Enter: '))
    tuple2_in_list = list(list_of_tuples[1])
    tuple2_in_list [2] = input2
    input3 = int(input('Enter third number and press Enter: '))
    tuple3_in_list = list(list_of_tuples[2])
    tuple3_in_list[1] = input3
    print('Сhanged the last values ​​of each tuple: \n',
          [tuple(tuple1_in_list),tuple(tuple2_in_list),tuple(tuple3_in_list)])
    if True==True:
        break
