# Now you have to write a function that takes an argument and returns the square of it.

def square(n: int) -> int:
    return n ** 2


if __name__ == '__main__':
    assert square(2) == 4
    assert square(50) == 2500
    assert square(1) == 1
