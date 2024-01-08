def solution(text: str) -> str:
    return ''.join(f' {char}' if char.isupper() else char
                   for char in text)



if __name__ == '__main__':
    print(solution("helloWorld"))

    assert solution("helloWorld") == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution("breakCamelCase") == "break Camel Case"