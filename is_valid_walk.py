def is_valid_walk(walk: list) -> bool:
    if len(walk) != 10:
        return False

    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

    # coords = {'SN': 0, 'EW': 0}
    #
    # for s in walk:
    #     if s == 'n':
    #         coords['SN'] -= 1
    #     elif s == 's':
    #         coords['SN'] += 1
    #     elif s == 'w':
    #         coords['EW'] += 1
    #     elif s == 'e':
    #         coords['EW'] -= 1
    #
    # return coords['EW'] == 0 and coords['SN'] == 0


if __name__ == '__main__':
    print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
    print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))

    assert is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is True
    assert is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']) is False
    assert is_valid_walk(['w']) is False
    assert is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is False
