# Day 5: Learning File I/O and Exception Handling

# File I/O
file_path = "example.txt"

# Writing to a file
with open(file_path, 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a test file.\n")

# Reading from a file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# Exception Handling
try:
    with open("non_existent_file.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
