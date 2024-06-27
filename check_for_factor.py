def check_for_factor(base: int, factor: int) -> bool:
    return base % factor == 0


if __name__ == '__main__':
    print(check_for_factor(24612, 3))

    assert check_for_factor(10, 2) is True
    assert check_for_factor(63, 7) is True
    assert check_for_factor(2450, 5) is True
    assert check_for_factor(24612, 3) is True
