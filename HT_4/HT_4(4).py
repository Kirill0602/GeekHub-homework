'''
4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
'''
string_input = input('Enter an arbitrary string with characters, numbers, letters: \n')

def sorting_string(string_input):
    renter = int(len(string_input))
    
    if 30 < renter <= 50:
        nums = ''
        letters = ''
        for c in string_input:
            if c.isdigit():
                nums = nums + c
            if c.isalpha():
                letters = letters + c
        return 'String length: {}, string: {}, numbers: {}'.format(len(string_input), letters, nums)
    
    if renter < 30:
        nums = 0
        letters = ''
        for x in string_input:
            if x.isdigit():
                nums += int(x)
            if x.isalpha():
                letters = letters + x
        return 'Sum of numbers: {}, string: {}'.format(nums, letters)
        
    if renter > 50:
        result = renter - 50
        return 'The length of the entered elements {}. It is more than 50 on {}'.format(renter, result)
    
    


print(sorting_string(string_input))
