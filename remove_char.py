def remove_char(s: str) -> str:
    return s[1:-1]


if __name__ == '__main__':
    print(remove_char('country'))
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''
    assert remove_char('ooopsss') == 'oopss'
