# def order(sentence: str) -> str:
#     dt = {}
#     for word in sentence.split():
#         for char in word:
#             if char.isdigit():
#                 dt[char] = word
#
#     return ' '.join(map(lambda x: x[1], sorted(dt.items())))

def order(sentence: str) -> str:
    return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))  # сортировка по ключу, каждое слово, сортируется


if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))

    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert order("") == ""
