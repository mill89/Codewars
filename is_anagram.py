def is_anagram(test: str, original: str) -> bool:
    return sorted(test.lower()) == sorted(original.lower())


if __name__ == '__main__':
    assert is_anagram("foefet", "toffee") is True
    assert is_anagram("Buckethead", "DeathCubeK"), True
    assert is_anagram("Twoo", "WooT") is True
    assert is_anagram("dumble", "bumble") is False
    assert is_anagram("ound", "round") is False
    assert is_anagram("apple", "pale") is False
