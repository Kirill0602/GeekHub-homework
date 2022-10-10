#2. Write a script which accepts two sequences of comma-separated colors from user. 
#Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = input()
color_list_2 = input()
color_list_1 = set(color_list_1.split(sep=', '))
color_list_2 = set(color_list_2.split(sep=', '))
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
