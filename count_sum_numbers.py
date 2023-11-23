# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


# def count_positives_sum_negatives(arr: list) -> list:
#     pos, neg = 0, 0
#
#     if not arr:
#         return []
#     for n in arr:
#         if n > 0:
#             pos += 1
#         else:
#             neg += n
#     return [pos, neg]

def count_positives_sum_negatives(arr: list) -> list:
    if arr:
        return [sum(1 for n in arr if n > 0), sum(n for n in arr if n < 0)]
    return []


if __name__ == '__main__':
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -11, -12, -13, -14, -15]))
    print(count_positives_sum_negatives([-1]))
    print(count_positives_sum_negatives([0]))
    print(count_positives_sum_negatives([]))

    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
    assert count_positives_sum_negatives([1]) == [1, 0]
    assert count_positives_sum_negatives([-1]) == [0, -1]
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
    assert count_positives_sum_negatives([]) == []
