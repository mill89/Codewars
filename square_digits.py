def square_digits(num: int) -> int:
    return int(''.join(str(int(n) ** 2)
                       for n in str(num)))


if __name__ == '__main__':
    print(square_digits(99563154))

    # assert square_digits(9119) == 811181
    # assert square_digits(0) == 0
