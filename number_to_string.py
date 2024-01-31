def number_to_string(n: int) -> str:
    return str(n)


if __name__ == '__main__':
    assert number_to_string(67) == '67'
    assert number_to_string(79585) == '79585'
    assert number_to_string(79585) == "79585"
    assert number_to_string(1 + 2) == '3'
    assert number_to_string(1 - 2) == '-1'

    print(number_to_string(1 + 2))
