'''
3. Write a script to concatenate the following dictionaries to create a NEW one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}
'''



print('First dictionary: ', {'foo': 'bar', 'bar': 'buz'})
print('Second dictionary: ', {'dou': 'jones', 'USD': 36})
print('Third dictionary: ', {'AUD': 19.2, 'name': 'Tom'})

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
dict_4 = {}

for d in (dict_1, dict_2, dict_3):
    dict_4.update(d)
    
print('Concatenate dictionary: \n', dict_4)
    
