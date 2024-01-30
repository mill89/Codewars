def make_upper_case(s: str) -> str:
    return s.upper()


if __name__ == '__main__':
    assert make_upper_case("hello") == "HELLO"

    print(make_upper_case("hello"))
