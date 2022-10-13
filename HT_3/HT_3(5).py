'''
5. Write a script to remove values duplicates from dictionary.
Feel free to hardcode your dictionary.
'''

dict_1 = {'foo': 'bar', 'name': 'Tom', 'beer': 'bar'}
print('Dictionary : ', dict_1)

result = {}

for key, value in dict_1.items():
    if value not in result.values():
        result[key] = value
print('Remove values duplicates:\n',result)
