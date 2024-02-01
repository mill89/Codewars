def wave(people: str) -> list:
    return [''.join([char.upper() if n == i else char
                     for n, char in enumerate(people)])
            for i, letter in enumerate(people)
            if letter != ' ']


def wave2(text: str) -> list:
    # capitalize - Начинает строку с заглавной буквы, форматируем строку с помощью срезов
    return [text[:n].lower() + text[n:].capitalize()
            for n in range(len(text))
            if text[n] != " "]  # пропускаем пробел, если есть


if __name__ == '__main__':
    assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave('codewars') == ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs",
                                "codewarS"]
    assert wave('two words') == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds",
                                 "two worDs", "two wordS"]
    assert wave('this is a few words') == ["This is a few words", "tHis is a few words", "thIs is a few words",
                                           "thiS is a few words", "this Is a few words", "this iS a few words",
                                           "this is A few words", "this is a Few words", "this is a fEw words",
                                           "this is a feW words", "this is a few Words", "this is a few wOrds",
                                           "this is a few woRds", "this is a few worDs", "this is a few wordS"]

    print(wave2('this is a few words'))
