# Tuples are immutable, so they don't have many methods. 
# However, you can perform several operations with tuples.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)  # Output: (1, 2, 3, 4, 5)

# count()
print("count of 3:", my_tuple.count(3))  # Output: 1

# index()
print("index of 4:", my_tuple.index(4))  # Output: 3

# Accessing elements
print("Element at index 1:", my_tuple[1])  # Output: 2

# Slicing
print("Slice [1:3]:", my_tuple[1:3])  # Output: (2, 3)

# Negative indexing
print("Last element:", my_tuple[-1])  # Output: 5

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Concatenated tuple:", tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
print("Repeated tuple:", tuple1 * 3)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
print("Length of tuple:", len(my_tuple))  # Output: 5

# Membership
print("Is 3 in tuple:", 3 in my_tuple)  # Output: True

# Iteration
print("Elements in tuple:")
for item in my_tuple:
    print(item)
# Output: 
# 1
# 2
# 3
# 4
# 5

# Tuple packing and unpacking
a, b, c = 1, 2, 3  # Packing
my_tuple = (a, b, c)  # Unpacking
print("Packed tuple:", my_tuple)  # Output: (1, 2, 3)
a, b, c = my_tuple
print("Unpacked values:", a, b, c)  # Output: 1 2 3

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)  # Output: ((1, 2), (3, 4), (
