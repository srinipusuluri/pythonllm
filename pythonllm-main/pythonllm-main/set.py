# add()
my_set = {1, 2, 3}
my_set.add(4)
print("add:", my_set)  # Output: {1, 2, 3, 4}

# clear()
my_set = {1, 2, 3}
my_set.clear()
print("clear:", my_set)  # Output: set()

# copy()
my_set = {1, 2, 3}
new_set = my_set.copy()
print("copy:", new_set)  # Output: {1, 2, 3}

# difference()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("difference:", set1.difference(set2))  # Output: {1}

# difference_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print("difference_update:", set1)  # Output: {1}

# discard()
my_set = {1, 2, 3}
my_set.discard(2)
print("discard:", my_set)  # Output: {1, 3}

# intersection()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("intersection:", set1.intersection(set2))  # Output: {2, 3}

# intersection_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print("intersection_update:", set1)  # Output: {2, 3}

# isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("isdisjoint:", set1.isdisjoint(set2))  # Output: True

# issubset()
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("issubset:", set1.issubset(set2))  # Output: True

# issuperset()
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print("issuperset:", set1.issuperset(set2))  # Output: True

# pop()
my_set = {1, 2, 3}
popped_item = my_set.pop()
print("pop:", my_set)  # Output: {2, 3} or {1, 3} or {1, 2} (sets are unordered)
print("popped item:", popped_item)  # Output: 1 or 2 or 3

# remove()
my_set = {1, 2, 3}
my_set.remove(2)
print("remove:", my_set)  # Output: {1, 3}

# symmetric_difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("symmetric_difference:", set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# symmetric_difference_update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update:", set1)  # Output: {1, 2, 4, 5}

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("union:", set1.union(set2))  # Output: {1, 2, 3, 4, 5}

# update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print("update:", set1)  # Output: {1, 2, 3, 4, 5}

# Frozenset (immutable set)
my_set = frozenset([1, 2, 3])
print("frozenset:", my_set)  # Output: frozenset({1, 2, 3})

# Using set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
print("union:", set1 | set2)  # Output: {1, 2, 3, 4, 5}
# Intersection
print("intersection:", set1 & set2)  # Output: {3}
# Difference
print("difference:", set1 - set2)  # Output: {1, 2}
# Symmetric Difference
print("symmetric difference:", set1 ^ set2)  # Output: {1, 2, 4, 5}
