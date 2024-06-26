def array_diff(a: list, b: list) -> list:
    return [n for n in a if n not in b]


if __name__ == '__main__':
    print(array_diff([1, 2, 2], [1]))

    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 2], [1]) == [2, 2]
    assert array_diff([1, 2, 2], [2]) == [1]
    assert array_diff([1, 2, 2], []) == [1, 2, 2]
    assert array_diff([], [1, 2]) == []
    assert array_diff([1, 2, 3], [1, 2]) == [3]
