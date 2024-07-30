def positive_sum(arr: list[int]) -> int:
    return sum(n for n in arr if n >= 0)


if __name__ == '__main__':
    assert positive_sum([1, 2, 3, 4, 5]) == 15
    assert positive_sum([1, -2, 3, 4, 5]) == 13
    assert positive_sum([-1, 2, 3, 4, -5]) == 9
