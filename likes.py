def likes(names: list) -> str:
    ln = len(names)
    if ln == 1:
        return names[0] + ' likes this'
    if ln == 2:
        return " and ".join(names) + ' like this'
    if ln == 3:
        return f'{names[0]}, {" and ".join(names[1:])} like this'
    if ln > 3:
        return f'{", ".join(names[:2])} and {ln - 2} others like this'
    return 'no one likes this'


if __name__ == '__main__':
    print(likes(['Alex', 'Jacob', 'tom', 'Alex', 'Jacob', 'Mark', 'Max']))

    assert likes([]) == 'no one likes this'
    assert likes(['Peter']) == 'Peter likes this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
