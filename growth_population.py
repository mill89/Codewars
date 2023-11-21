# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
# p0 = population,
# percent,
# aug (inhabitants coming or leaving each year),
# p (population to equal or surpass)
import math


def nb_year(p0: int, percent: int | float, aug: int, p: int) -> int:
    years = 0
    while p0 <= p:
        p0 += math.floor(p0 * (percent / 100)) + aug
        years += 1
    return years


if __name__ == '__main__':
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94

    print(nb_year(1500000, 2.5, 10000, 2000000))
    print(nb_year(1500000, 0.25, 1000, 2000000))
    print(nb_year(1500, 5, 100, 5000))
