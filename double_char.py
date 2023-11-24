# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(st: str) -> str:
    return ''.join(s * 2 for s in st)


if __name__ == '__main__':
    print(double_char("String"))

    assert double_char("String") == "SSttrriinngg"
    assert double_char("Hello World") == "HHeelllloo  WWoorrlldd"
    assert double_char("1234!_ ") == "11223344!!__  "
