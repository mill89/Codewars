from string import ascii_lowercase as AL


# def is_pangram(s: str) -> bool:
#     a = set(x for x in AL)
#     b = set(x for x in s.lower() if x in a)
#
#     return True if b.intersection(a) == a else False


def is_pangram(s: str) -> bool:
    return set(AL).issubset(s.lower())


if __name__ == '__main__':
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))

    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True
    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False
