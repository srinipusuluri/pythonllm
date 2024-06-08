# Day 2: Testing Your Learning

def test_day2():
    # Test If-Else
    x = 10
    if x > 5:
        assert True
    else:
        assert False

    # Test For Loop
    for i in range(5):
        assert i in range(5)

    # Test While Loop
    count = 0
    while count < 5:
        assert count < 5
        count += 1

    print("Day 2 tests passed!")

test_day2()
