# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)
#
# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

# def stray(arr: list) -> int:
#     for n in arr:
#         if arr.count(n) == 1:
#             return n


def stray(arr: list) -> int:
    return min(arr, key=arr.count)


if __name__ == '__main__':
    print(stray([1, 1, 1, 1, 1, 4, 1]))

    assert stray([1, 1, 1, 1, 1, 1, 2]) == 2
    assert stray([2, 3, 2, 2, 2]) == 3
    assert stray([3, 2, 2, 2, 2]) == 3
