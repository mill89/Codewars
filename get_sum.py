def get_sum(a: int, b: int) -> int:
    return sum(range(min(a, b), max(a, b) + 1))


if __name__ == '__main__':
    assert get_sum(1, 0) == 1
    assert get_sum(1, 2) == 3
    assert get_sum(0, 1) == 1
    assert get_sum(1, 1) == 1
    assert get_sum(-1, 0) == -1
    assert get_sum(-1, 2) == 2

    print(get_sum(1, 1))
    print(get_sum(54, 33))
    print(get_sum(1, 4))
