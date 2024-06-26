def solution(nums: any) -> any:
    return sorted(nums) if nums else []


if __name__ == '__main__':
    print(solution([1, 2, 3, 10, 5]))
    print(solution([1,  2,  3]))
    print(solution(None))

    assert solution([1, 2, 3, 10, 5]) == [1, 2, 3, 5, 10]
    assert solution(None) == []
    assert solution([]) == []
    assert solution([20, 2, 10]) == [2, 10, 20]
    assert solution([2, 20, 10]) == [2, 10, 20]
