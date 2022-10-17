string_input = input('Enter an arbitrary string with characters, numbers, letters: \n')

def sorting_string(string_input):
    
    if renter > 30 and renter <= 50:
        nums = ''
        letters = ''
        for c in string_input:
            if c.isdigit():
                nums = nums + c
            if c.isalpha():
                letters = letters + c
        return 'String length: %s, string: %s, numbers: %s' %(len(string_input), letters, nums)
    
    if renter < 30:
        nums = 0
        letters = ''
        for x in string_input:
            if x.isdigit():
                nums += int(x)
            if x.isalpha():
                letters = letters + x
        return 'Sum of numbers: %s, string: %s' %(nums, letters)
        
    if renter > 50:
        result = renter - 50
        return 'The length of the entered elements %s. It is more than 50 on %s' %(renter, result)
    
renter = int(len(string_input))    


print(sorting_string(string_input))
