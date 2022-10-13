year1 = int(input('Enter the initial year: '))
year2 = int(input('Enter еthe ending year: '))
print('All the high years in this interval:') 
for year in range(year1, year2+1):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)
        year += 1
       




