def reverse_words(text: str) -> str:
    return ' '.join(map(lambda s: s[::-1], text.split(' ')))


if __name__ == '__main__':
    print(reverse_words('double  spaced  words'))
    print(reverse_words('The quick brown fox jumps over the lazy dog.'))

    assert reverse_words(
        'The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    assert reverse_words('apple') == 'elppa'
    assert reverse_words('a b c d') == 'a b c d'
    assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'
