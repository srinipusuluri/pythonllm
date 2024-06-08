# Day 4: Testing Your Learning

def test_day4():
    # Test Lists
    fruits = ["apple", "banana", "cherry"]
    assert fruits[0] == "apple"
    fruits.append("orange")
    assert fruits[-1] == "orange"

    # Test Dictionaries
    student = {"name": "Alice", "age": 20, "is_student": True}
    assert student["name"] == "Alice"
    student["age"] = 21
    assert student["age"] == 21

    print("Day 4 tests passed!")

test_day4()
