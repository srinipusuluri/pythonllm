# append()
my_list = [1, 2, 3]
my_list.append(4)
print("append:", my_list)  # Output: [1, 2, 3, 4]

# extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print("extend:", my_list)  # Output: [1, 2, 3, 4, 5]

# insert()
my_list = [1, 2, 4]
my_list.insert(2, 3)
print("insert:", my_list)  # Output: [1, 2, 3, 4]

# remove()
my_list = [1, 2, 3, 4]
my_list.remove(3)
print("remove:", my_list)  # Output: [1, 2, 4]

# pop()
my_list = [1, 2, 3, 4]
removed_item = my_list.pop(2)
print("pop:", my_list)      # Output: [1, 2, 4]
print("popped item:", removed_item) # Output: 3

# clear()
my_list = [1, 2, 3, 4]
my_list.clear()
print("clear:", my_list)  # Output: []

# index()
my_list = [1, 2, 3, 4]
index = my_list.index(3)
print("index of 3:", index)  # Output: 2

# count()
my_list = [1, 2, 3, 2, 4]
count = my_list.count(2)
print("count of 2:", count)  # Output: 2

# sort()
my_list = [4, 1, 3, 2]
my_list.sort()
print("sorted list:", my_list)  # Output: [1, 2, 3, 4]

# reverse()
my_list = [1, 2, 3, 4]
my_list.reverse()
print("reversed list:", my_list)  # Output: [4, 3, 2, 1]

# copy()
my_list = [1, 2, 3, 4]
new_list = my_list.copy()
print("copied list:", new_list)  # Output: [1, 2, 3, 4]

# Additional examples

# Appending multiple items (using extend vs. append)
my_list = [1, 2, 3]
my_list.append([4, 5])
print("append list:", my_list)  # Output: [1, 2, 3, [4, 5]]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print("extend list:", my_list)  # Output: [1, 2, 3, 4, 5]

# Sorting with custom key
my_list = ["apple", "banana", "cherry"]
my_list.sort(key=len)
print("sorted by length:", my_list)  # Output: ['apple', 'cherry', 'banana']

# Using pop without an argument
my_list = [1, 2, 3, 4]
last_item = my_list.pop()
print("pop without argument:", my_list)    # Output: [1, 2, 3]
print("popped last item:", last_item)  # Output: 4


# append()
my_list = [1, 2, 3]
my_list.append(4)
print("append:", my_list)  # Output: [1, 2, 3, 4]

# extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print("extend:", my_list)  # Output: [1, 2, 3, 4, 5]

# insert()
my_list = [1, 2, 4]
my_list.insert(2, 3)
print("insert:", my_list)  # Output: [1, 2, 3, 4]

# remove()
my_list = [1, 2, 3, 4]
my_list.remove(3)
print("remove:", my_list)  # Output: [1, 2, 4]

# pop()
my_list = [1, 2, 3, 4]
removed_item = my_list.pop(2)
print("pop:", my_list)      # Output: [1, 2, 4]
print("popped item:", removed_item) # Output: 3

# clear()
my_list = [1, 2, 3, 4]
my_list.clear()
print("clear:", my_list)  # Output: []

# index()
my_list = [1, 2, 3, 4]
index = my_list.index(3)
print("index of 3:", index)  # Output: 2

# count()
my_list = [1, 2, 3, 2, 4]
count = my_list.count(2)
print("count of 2:", count)  # Output: 2

# sort()
my_list = [4, 1, 3, 2]
my_list.sort()
print("sorted list:", my_list)  # Output: [1, 2, 3, 4]

# reverse()
my_list = [1, 2, 3, 4]
my_list.reverse()
print("reversed list:", my_list)  # Output: [4, 3, 2, 1]

# copy()
my_list = [1, 2, 3, 4]
new_list = my_list.copy()
print("copied list:", new_list)  # Output: [1, 2, 3, 4]

# Additional examples

# Appending multiple items (using extend vs. append)
my_list = [1, 2, 3]
my_list.append([4, 5])
print("append list:", my_list)  # Output: [1, 2, 3, [4, 5]]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print("extend list:", my_list)  # Output: [1, 2, 3, 4, 5]

# Sorting with custom key
my_list = ["apple", "banana", "cherry"]
my_list.sort(key=len)
print("sorted by length:", my_list)  # Output: ['apple', 'cherry', 'banana']

# Using pop without an argument
my_list = [1, 2, 3, 4]
last_item = my_list.pop()
print("pop without argument:", my_list)    # Output: [1, 2, 3]
print("popped last item:", last_item)  # Output: 4

# Nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("nested list:", nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]

# Membership test
my_list = [1, 2, 3, 4]
print("3 in list:", 3 in my_list)  # Output: True

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("concatenated list:", concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = [1, 2, 3] * 3
print("repeated list:", repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Length
my_list = [1, 2, 3, 4]
print("length of list:", len(my_list))  # Output: 4

# Maximum and Minimum
num_list = [10, 20, 30, 40, 50]
print("max value:", max(num_list))  # Output: 50
print("min value:", min(num_list))  # Output: 10

# Summing all elements
print("sum of list:", sum(num_list))  # Output: 150

# Slicing
my_list = [1, 2, 3, 4, 5]
print("slice [1:3]:", my_list[1:3])  # Output: [2, 3]
print("slice [::2]:", my_list[::2])  # Output: [1, 3, 5]

