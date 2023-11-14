# In this kata you will create a function that takes a list of non-negative
# integers and strings and returns a new list with the strings filtered out.

def filter_list(l: list) -> list:
    return list(filter(lambda n: isinstance(n, int), l))


if __name__ == '__main__':
    print(filter_list([1, 2, 'a', 'b']))
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]
