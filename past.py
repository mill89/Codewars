# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59
# h = 60m
# m = 60s
# s = 1000ms


def past(h: int, m: int, s: int) -> int:
    return ((((h * 60) + m) * 60) + s) * 1000


if __name__ == '__main__':
    print(past(1, 0, 1))

    assert past(0, 1, 1) == 61000
    assert past(1, 1, 1) == 3661000
    assert past(0, 0, 0) == 0
    assert past(1, 0, 1) == 3601000
    assert past(1, 0, 0) == 3600000
