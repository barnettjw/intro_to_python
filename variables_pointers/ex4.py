dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a']) #  [1, 42, 3]

# because constructors make shallow copies
# shallow copies use references for nested objects