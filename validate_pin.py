def validate_pin(pin: str) -> bool:
    return pin.isdigit() and (len(pin) in (4, 6))


if __name__ == '__main__':
    print(validate_pin("-1234"))
    print(validate_pin("1234"))

    assert validate_pin("1") == False, "Wrong output for '1'"
    assert validate_pin("12") == False, "Wrong output for '12'"
    assert validate_pin("123") == False, "Wrong output for '123'"
    assert validate_pin("12345") == False, "Wrong output for '12345'"
    assert validate_pin("1234567") == False, "Wrong output for '1234567'"
    assert validate_pin("-1234") == False, "Wrong output for '-1234'"
    assert validate_pin("-12345") == False, "Wrong output for '-12345'"
    assert validate_pin("1.234") == False, "Wrong output for '1.234'"
    assert validate_pin("00000000") == False, "Wrong output for '00000000'"
    assert validate_pin("a234") == False, "Wrong output for 'a234'"
    assert validate_pin(".234") == False, "Wrong output for '.234'"
    assert validate_pin("1234") == True, "Wrong output for '1234'"
    assert validate_pin("0000") == True, "Wrong output for '0000'"
    assert validate_pin("1111") == True, "Wrong output for '1111'"
    assert validate_pin("123456") == True, "Wrong output for '123456'"
    assert validate_pin("098765") == True, "Wrong output for '098765'"
    assert validate_pin("000000") == True, "Wrong output for '000000'"
    assert validate_pin("123456") == True, "Wrong output for '123456'"
    assert validate_pin("090909") == True, "Wrong output for '090909'"
