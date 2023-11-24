# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# def get_count(sentence: str) -> int:
#     vovels, count = 'aeiou', 0
#     for char in sentence:
#         if char in vovels:
#             count += 1
#     return count

def get_count(sentence: str) -> int:
    return sum(1 for letter in sentence if letter in 'aeiou')


if __name__ == '__main__':
    print(get_count("abracadabra"))

    assert get_count("aeiou") == 5
    assert get_count("bcdfghjklmnpqrstvwxzy") == 0
    assert get_count("abracadabra") == 5
