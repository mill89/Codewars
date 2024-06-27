def sale_hotdogs(n: int) -> int:
    # n < 5 == 100
    # n >= 5 and n < 10 == 95
    # n >= 10 == 90
    match n:
        case _ if n < 5:
            return n * 100
        case _ if 5 <= n < 10:
            return n * 95
        case _ if n >= 10:
            return n * 90


# def sale_hotdogs(n):
#     return (100, 95, 90)[(n > 4) + (n > 9)] * n



if __name__ == '__main__':
    print(sale_hotdogs(123))

    assert sale_hotdogs(0) == 0
    assert sale_hotdogs(1) == 100
    assert sale_hotdogs(2) == 200
    assert sale_hotdogs(3) == 300
    assert sale_hotdogs(4) == 400
    assert sale_hotdogs(5) == 475
    assert sale_hotdogs(9) == 855
    assert sale_hotdogs(10) == 900
    assert sale_hotdogs(11) == 990
    assert sale_hotdogs(100) == 9000
