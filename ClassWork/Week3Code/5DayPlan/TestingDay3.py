# Day 3: Testing Your Learning

def test_day3():
    def greet(name):
        return f"Hello, {name}!"

    def add(x, y):
        return x + y

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    assert greet("Alice") == "Hello, Alice!"
    assert add(5, 3) == 8
    assert factorial(5) == 120

    print("Day 3 tests passed!")

test_day3()
