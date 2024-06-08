# Day 5: Testing Your Learning

def test_day5():
    import os

    # Test File I/O
    file_path = "example.txt"
    
    # Writing to a file
    with open(file_path, 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is a test file.\n")

    # Reading from a file
    with open(file_path, 'r') as file:
        content = file.read()
        assert "Hello, world!" in content
        assert "This is a test file." in content

    # Clean up
    os.remove(file_path)

    # Test Exception Handling
    try:
        with open("non_existent_file.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        assert True
    except Exception as e:
        assert False, f"Unexpected error occurred: {e}"

    print("Day 5 tests passed!")

test_day5()
