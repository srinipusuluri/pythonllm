# Day 3: Learning Functions

def greet(name):
    return f"Hello, {name}!"

def add(x, y):
    return x + y

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(greet("Alice"))
print(f"Sum: {add(5, 3)}")
print(f"Factorial: {factorial(5)}")
