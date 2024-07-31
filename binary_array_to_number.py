def binary_array_to_number(arr: list[int]) -> int:
    return int(''.join(map(str, arr)), 2)


if __name__ == '__main__':
    print(binary_array_to_number([1, 1, 1, 1]))

    assert binary_array_to_number([0, 0, 0, 1]) == 1
    assert binary_array_to_number([0, 0, 1, 0]) == 2
    assert binary_array_to_number([1, 1, 1, 1]) == 15
    assert binary_array_to_number([0, 1, 1, 0]) == 6
