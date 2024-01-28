def other_angle(a: int, b: int) -> int:
    return 180 - (a + b)


if __name__ == '__main__':
    assert other_angle(30, 60) == 90
    assert other_angle(60, 60) == 60
    assert other_angle(43, 78) == 59
    assert other_angle(10, 20) == 150

    print(other_angle(30, 60))
