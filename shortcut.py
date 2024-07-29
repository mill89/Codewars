def shortcut(s: str) -> str:
    return ''.join(n for n in s if n not in ('aeiou'))


if __name__ == '__main__':
    print(shortcut("how are you today?"))

    assert shortcut("hello") == "hll"
    assert shortcut("hellooooo") == "hll"
    assert shortcut("how are you today?") == "hw r y tdy?"
    assert shortcut("complain") == "cmpln"
    assert shortcut("never") == "nvr"
