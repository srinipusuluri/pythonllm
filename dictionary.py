# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# clear()
my_dict.clear()
print("clear:", my_dict)  # Output: {}

# copy()
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()
print("copy:", new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# fromkeys()
keys = ('a', 'b', 'c')
value = 0
new_dict = dict.fromkeys(keys, value)
print("fromkeys:", new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# get()
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("get 'b':", my_dict.get('b'))  # Output: 2
print("get 'd' with default:", my_dict.get('d', 'default'))  # Output: default

# items()
print("items:", my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys()
print("keys:", my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# values()
print("values:", my_dict.values())  # Output: dict_values([1, 2, 3])

# pop()
popped_value = my_dict.pop('b')
print("pop 'b':", popped_value)  # Output: 2
print("dictionary after pop:", my_dict) 
