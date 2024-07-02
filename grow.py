def grow(arr: list[int]) -> int:
    return eval(' * '.join(map(str, arr)))

    # res = 1
    # for n in arr:
    #     res *= n
    # return res


if __name__ == '__main__':
    print(grow([4, 1, 1, 1, 4]))

    assert grow([1, 2, 3]) == 6
    assert grow([4, 1, 1, 1, 4]) == 16
    assert grow([2, 2, 2, 2, 2, 2]) == 64
