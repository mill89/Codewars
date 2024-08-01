def sort_by_length(arr: list[str]) -> list[str]:
    return sorted(arr, key=len)


if __name__ == '__main__':
    tests = [
        [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
        [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
        [["short", "longer", "longest"], ["longer", "longest", "short"]],
        [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
        [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
        [["a short sentence", "a longer sentence", "the longest sentence"],
         ["a longer sentence", "the longest sentence", "a short sentence"]],
    ]
    for t in tests:
        try:
            print(t[0])
            print(t[1])
            assert sort_by_length(t[1]) == t[0]
            print(f"code: 0 > {t[0]}")
            print("-" * 80)
        except AssertionError:
            print(f'error "{t[1]}" != {sort_by_length(t[0])}')
