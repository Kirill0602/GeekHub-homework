'''
2. Write a script to remove empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
'''

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
print('List:', test_list)
print('Remove empty elements: \n', list(filter(None, test_list)))
