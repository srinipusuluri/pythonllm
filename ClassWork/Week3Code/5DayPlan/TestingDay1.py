# Day 1: Testing Your Learning

def test_day1():
    # Test Variables
    a = 5
    b = 3.5
    name = "John"
    is_student = True

    assert type(a) == int
    assert type(b) == float
    assert type(name) == str
    assert type(is_student) == bool

    # Test Basic Operations
    assert a + b == 8.5
    assert a - b == 1.5
    assert a * b == 17.5
    assert a / b == 5 / 3.5

    print("Day 1 tests passed!")

test_day1()
