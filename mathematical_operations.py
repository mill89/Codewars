# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/python
# Examples(Operator, value1, value2) --> output

def basic_op(operator: str, value1: int, value2: int) -> int:
    return eval(f'{value1}{operator}{value2}')


if __name__ == '__main__':
    print(basic_op('+', 4, 7))
    assert basic_op('+', 4, 7) == 11
    assert basic_op('-', 15, 18) == -3
    assert basic_op('*', 5, 5) == 25
    assert basic_op('/', 49, 7) == 7
