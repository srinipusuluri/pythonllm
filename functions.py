# Functions

# Example of a simple function
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Result of addition:", result)  # Output: Result of addition: 8

# Function with default argument
def multiply(a, b=2):
    return a * b

result = multiply(3)
print("Result of multiplication:", result)  # Output: Result of multiplication: 6

# Function with variable number of arguments
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_all(1, 2, 3, 4, 5)
print("Result of adding all numbers:", result)  # Output: Result of adding all numbers: 15

# Classes and Methods

# Example of a simple class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says woof!")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", "Labrador")
print("Dog's name:", my_dog.name)  # Output: Dog's name: Buddy
print("Dog's breed:", my_dog.breed)  # Output: Dog's breed: Labrador
my_dog.bark()  # Output: Buddy says woof!

# Class with methods
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

# Creating an instance of the Calculator class
calc = Calculator()
print("Addition result:", calc.add(5, 3))  # Output: Addition result: 8
print("Subtraction result:", calc.subtract(5, 3))  # Output: Subtraction result: 2
print("Multiplication result:", calc.multiply(5, 3))  # Output: Multiplication result: 15
print("Division result:", calc.divide(10, 2))  # Output: Division result: 5.0
print("Division result:", calc.divide(10, 0))  # Output: Division result: Cannot divide by zero
