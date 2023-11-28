# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the
# input parameters, including them.
# For example:
#
# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a: int, b: int) -> list:
    return list(range(a, b + 1))


if __name__ == '__main__':
    print(between(1, 7))

    assert between(1, 4) == [1, 2, 3, 4]
    assert between(-2, 2) == [-2, -1, 0, 1, 2]
