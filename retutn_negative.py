# https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

# def make_negative(number: int) -> int:
#     if number < 0 or number == 0:
#         return number
#     return -number


def make_negative(number: int) -> int:
    return -abs(number)


if __name__ == '__main__':
    print(make_negative(256))

    assert make_negative(1) == -1
    assert make_negative(-5) == -5
    assert make_negative(0) == 0
