def remove_smallest(numbers: list[int]) -> list:
    if not numbers:
        return []
    copy_num = numbers[:]
    copy_num.remove(min(numbers))
    return copy_num


if __name__ == '__main__':
    print(remove_smallest([5, 3, 2, 1, 4]))

    assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
    assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
    assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
    assert remove_smallest([69, 147, 20, 369, 280]) == [69, 147, 369, 280]
    assert remove_smallest([]) == []
