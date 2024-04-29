def row_sum_odd_numbers(n: int) -> int:
    return n ** 3



if __name__ == '__main__':
    print(row_sum_odd_numbers(3))

    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
    assert row_sum_odd_numbers(19) == 6859
    assert row_sum_odd_numbers(41) == 68921
