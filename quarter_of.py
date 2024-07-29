import math


def quarter_of(month: int) -> int:
    return math.ceil(month / 3)


assert quarter_of(3) == 1
assert quarter_of(8) == 3
assert quarter_of(11) == 4
assert quarter_of(9) == 3
assert quarter_of(12) == 4
assert quarter_of(2) == 1
