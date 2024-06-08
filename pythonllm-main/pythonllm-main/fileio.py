import os

# Sample data to write to files
sample_data = [
    "Vehicle Make,Model,Year,Mileage\n",
    "Honda,Civic,2016,50000\n",
    "Toyota,Corolla,2018,40000\n",
    "Ford,F-150,2015,60000\n"
]

# Function to write to a file
def write_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.writelines(data)
        print(f"Data written to {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Function to read from a file
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Content of {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
    except IOError as e:
        print(f"Error reading file: {e}")

# Function to append to a file
def append_to_file(file_path, data):
    try:
        with open(file_path, 'a') as file:
            file.writelines(data)
        print(f"Data appended to {file_path}")
    except IOError as e:
        print(f"Error appending to file: {e}")

# Function to read a file line by line
def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  # end='' to avoid adding extra new lines
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
    except IOError as e:
        print(f"Error reading file: {e}")

# Function to read file using different modes
def read_file_modes(file_path):
    try:
        with open(file_path, 'r') as file:
            print("Reading entire file:")
            print(file.read())

        with open(file_path, 'r') as file:
            print("Reading file line by line:")
            for line in file:
                print(line, end='')

        with open(file_path, 'r') as file:
            print("\nReading file using readlines():")
            lines = file.readlines()
            for line in lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
    except IOError as e:
        print(f"Error reading file: {e}")

# Function to handle file not found exception
def handle_file_not_found(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Content of {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found")

# Function to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} deleted successfully")
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
    except IOError as e:
        print(f"Error deleting file: {e}")

# Define file paths
file_path = "vehicles.csv"
non_existing_file_path = "non_existing_file.csv"

# Write to a file
write_to_file(file_path, sample_data)

# Read from a file
read_from_file(file_path)

# Append to a file
append_to_file(file_path, ["Chevrolet,Malibu,2017,45000\n"])

# Read from a file line by line
read_file_line_by_line(file_path)

# Read file using different modes
read_file_modes(file_path)

# Handle file not found exception
handle_file_not_found(non_existing_file_path)

# Delete a file
#delete_file(file_path)
