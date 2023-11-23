# Write a function that checks if a given string (case insensitive) is a palindrome.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as
# forwards, such as madam or racecar.

def is_palindrome(word: str) -> bool:
    return word.lower() == word.lower()[::-1]


if __name__ == '__main__':
    print(is_palindrome('a'))
    print(is_palindrome('walter'))
    print(is_palindrome('malam'))

    assert is_palindrome('a') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('Abba') == True
    assert is_palindrome('malam') == True
    assert is_palindrome('walter') == False
    assert is_palindrome('kodok') == True
    assert is_palindrome('Kasue') == False
