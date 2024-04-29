def get_age(age: str) -> int:
    return int(age[0])

def get_age2(age: int) -> str:
    if age == 1:
        return f'{age} year old'
    return f'{age} years old'


if __name__ == '__main__':
    print(get_age("2 years old"))
    print(get_age2(5))
    print(get_age2(1))

    assert get_age("2 years old") == 2
    assert get_age("4 years old") == 4
    assert get_age("5 years old") == 5
    assert get_age("7 years old") == 7
