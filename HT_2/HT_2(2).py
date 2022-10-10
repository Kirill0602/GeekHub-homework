#2. Write a script which accepts two sequences of comma-separated colors from user. 
#Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

first_input_colors = input('Enter the first list of colors: \n')
second_input_colors = input('Enter the second list of colors: \n')

color_list_1 = set(first_input_colors.split())
color_list_2 = set(second_input_colors.split())

print("\nColors that are not in the second list:")
print(color_list_1.difference(color_list_2))
