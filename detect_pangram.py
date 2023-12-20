import string


# def is_pangram(s: str) -> bool:
#     a = set(x for x in string.ascii_lowercase)
#     b = set(x for x in s.lower() if x in a)
#
#     return True if b.intersection(a) == a else False


def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())


if __name__ == '__main__':
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
    c = 1
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True
    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False
