def find_smallest_int(arr: list) -> int:
    return min(arr)


if __name__ == '__main__':
    print(find_smallest_int([78, 56, 232, 12, 11, 43]))

    assert find_smallest_int([78, 56, 232, 12, 11, 43]) == 11
    assert find_smallest_int([78, 56, -2, 12, 8, -33]) == -33
    assert find_smallest_int([0, 1 - 2 ** 64, 2 ** 64]) == 1 - 2 ** 64