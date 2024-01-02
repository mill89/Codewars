def bool_to_word(_boolean: bool) -> str:
    return 'Yes' if _boolean else 'No'


if __name__ == '__main__':
    assert bool_to_word(True) == 'Yes'
    assert bool_to_word(False) == 'No'
