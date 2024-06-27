def gimme(input_array: list) -> int:
    mid = sorted(input_array)[1]
    return input_array.index(mid)


    # mn = input_array.index(min(input_array))
    # mx = input_array.index(max(input_array))
    # return 3 - (mn + mx)


if __name__ == '__main__':
    assert gimme([2, 3, 1]) == 0
    assert gimme([5, 10, 14]) == 1
