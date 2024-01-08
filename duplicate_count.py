def duplicate_count(text: str) -> int:
    text = text.lower()
    return sum(1 for char in set(text)
               if text.count(char) > 1)


if __name__ == '__main__':
    print(duplicate_count("abcde"))

    assert duplicate_count("") == 0
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdeaa") == 1
    assert duplicate_count("abcdeaB") == 2
    assert duplicate_count("Indivisibilities") == 2
