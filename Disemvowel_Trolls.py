def disemvowel(string_):
    vowels = 'aeiouAEIOU'

    return ''.join(s for s in string_ if s not in vowels)


if __name__ == '__main__':
    print(disemvowel('This website is for losers LOL!'))
