def solution(text: str) -> str:
    return text[::-1]


if __name__ == '__main__':
    print(solution('world'))

    assert solution('world') == 'dlrow'
    assert solution('hello') == 'olleh'
    assert solution('') == ''
    assert solution('h') == 'h'
