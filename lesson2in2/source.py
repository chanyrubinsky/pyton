def is_adult(age):
    if age >= 18:
        return True
    return False


def test_1():
    result = is_adult(3)
    assert result == False


def test_2():
    result = is_adult(20)
    assert result == True
