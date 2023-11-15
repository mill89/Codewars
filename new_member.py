# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/python

def open_or_senior(data: list) -> list:
    return ['Senior' if x[0] > 54 and x[1] > 7 else 'Open' for x in data]


if __name__ == '__main__':
    print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
    assert open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]) == ['Open', 'Senior', 'Open', 'Senior']
    assert open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]) == ['Open', 'Open', 'Senior', 'Open']
