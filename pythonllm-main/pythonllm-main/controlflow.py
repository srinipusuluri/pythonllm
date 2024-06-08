# if, elif, else

# Example of if statement
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# Example of if-else statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")  # Output: x is not greater than 5

# Example of if-elif-else statement
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")  # Output: x is greater than 5 but less than or equal to 10
else:
    print("x is 5 or less")

# Nested if statements
x = 8
if x > 5:
    if x % 2 == 0:
        print("x is greater than 5 and even")  # Output: x is greater than 5 and even
    else:
        print("x is greater than 5 and odd")

# for loop

# Iterating over a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5

# Iterating over a string
word = "hello"
for letter in word:
    print(letter)
# Output:
# h
# e
# l
# l
# o

# Using range()
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Using range() with start and end
for i in range(2, 6):
    print(i)
# Output:
# 2
# 3
# 4
# 5

# Using range() with start, end, and step
for i in range(1, 10, 2):
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

# while loop

# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4

# Using break

# Example with for loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Example with while loop
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4

# Using continue

# Example with for loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

# Example with while loop
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
# Output:
# 1
# 3
# 5
# 7
# 9

# Using pass

# pass in if-else
x = 10
if x > 5:
    pass  # Do nothing
else:
    print("x is not greater than 5")

# pass in for loop
for i in range(10):
    if i % 2 == 0:
        pass  # Do nothing
    else:
        print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

# pass in while loop
count = 0
while count < 5:
    count += 1
    pass  # Do nothing
print("Loop finished")  # Output: Loop finished
