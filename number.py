def number(lines: list) -> list:
    return [f'{n}: {st}' for n, st in enumerate(lines, 1)]


if __name__ == '__main__':
    assert number([]) == []
    assert number(["a", "b", "c"]) ==["1: a", "2: b", "3: c"]

    print(number(["a", "b", "c"]))
