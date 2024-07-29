def nb_dig(n: int, d: int) -> int:
    sq_list = [str(num ** 2) for num in range(n + 1)]
    count_d = 0
    for s in sq_list:
        if str(d) in s:
            count_d += s.count(str(d))

    return count_d
    # return sum(str(num ** 2).count(str(d)) for num in range(n + 1) if str(d) in str(num ** 2))


if __name__ == '__main__':
    assert nb_dig(10, 1) == 4
    assert nb_dig(5750, 0) == 4700
    assert nb_dig(11011, 2) == 9481
    assert nb_dig(12224, 8) == 7733
    assert nb_dig(11549, 1) == 11905
    assert nb_dig(14550, 7) == 8014
    assert nb_dig(8304, 7) == 3927
    assert nb_dig(10576, 9) == 7860
    assert nb_dig(12526, 1) == 13558
    assert nb_dig(7856, 4) == 7132
    assert nb_dig(14956, 1) == 17267
