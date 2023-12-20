# def solution(text: str, ending: str) -> bool:
#     return ending in text and ending[-1] == text[-1]

def solution(string: str, ending: str) -> bool:
    return string.endswith(ending)

if __name__ == '__main__':
    assert solution("samurai", "ai") == True
    assert solution("ninja", "ja") == True
    assert solution("sensei", "i") == True
    assert solution("abc", "abc") == True
    assert solution("abcabc", "bc") == True
    assert solution("fails", "ails") == True
    assert solution("sumo", "omo") == False
    assert solution("samurai", "ra") == False
    assert solution("abc", "abcd") == False
    assert solution("ails", "fails") == False
    assert solution("this", "fails") == False
    assert solution("spam", "eggs") == False
