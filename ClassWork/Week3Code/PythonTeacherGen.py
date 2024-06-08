# Python Basics: Variables, Data Types, Operators, Statements, and File I/O

# 1. Variables
print("1. Variables:")
# A variable is used to store data. You can assign a value to a variable using the assignment operator (=).
x = 10
y = 5
name = "Alice"
print(f"x = {x}, y = {y}, name = {name}\n")

# 2. Data Types
print("2. Data Types:")
# Python supports several data types, including integers, floats, strings, and booleans.
integer_var = 42        # Integer
float_var = 3.14        # Float
string_var = "Hello"    # String
boolean_var = True      # Boolean
print(f"integer_var = {integer_var} (type: {type(integer_var)})")
print(f"float_var = {float_var} (type: {type(float_var)})")
print(f"string_var = '{string_var}' (type: {type(string_var)})")
print(f"boolean_var = {boolean_var} (type: {type(boolean_var)})\n")

# 3. Operators
print("3. Operators:")
# Python has various operators for arithmetic, comparison, and logical operations.
a = 15
b = 4
# Arithmetic operators
sum_result = a + b          # Addition
diff_result = a - b         # Subtraction
product_result = a * b      # Multiplication
quotient_result = a / b     # Division
modulus_result = a % b      # Modulus
exponent_result = a ** b    # Exponentiation
print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {diff_result}")
print(f"{a} * {b} = {product_result}")
print(f"{a} / {b} = {quotient_result}")
print(f"{a} % {b} = {modulus_result}")
print(f"{a} ** {b} = {exponent_result}\n")

# Comparison operators
print(f"{a} > {b} = {a > b}")
print(f"{a} < {b} = {a < b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")

# Logical operators
x = True
y = False
print(f"x and y = {x and y}")
print(f"x or y = {x or y}")
print(f"not x = {not x}\n")

# 4. Statements
print("4. Statements:")
# Conditional statements
num = 10
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Loops
print("While Loop:")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

print("For Loop:")
for i in range(5):
    print(f"Iteration: {i}")
print()

# 5. File I/O
print("5. File I/O:")
# Writing to a file
file_path = "example.txt"
with open(file_path, 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")

# Reading from a file
with open(file_path, 'r') as file:
    content = file.read()
print("File Content:")
print(content)

# 6. Generating Python Code
print("6. Generating Python Code:")
# Let's create a simple Python script dynamically
script_content = """
# This is a dynamically generated Python script
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
"""

# Write the generated script to a file
script_path = "generated_script.py"
with open(script_path, 'w') as file:
    file.write(script_content)

print(f"Generated script saved to {script_path}")

# You can run the generated script in a Python environment
print("To run the generated script, execute the following command in your terminal:")
print(f"python {script_path}")
