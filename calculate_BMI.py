# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
# Write function bmi that calculates body mass index (bmi = weight / height2).

# def bmi(weight: int | float, height: int | float) -> str:
#     i = weight / height ** 2
#
#     if i <= 18.5:
#         return "Underweight"
#     elif i <= 25.0:
#         return "Normal"
#     elif i <= 30.0:
#         return "Overweight"
#     return "Obese"


def bmi(weight: int | float, height: int | float) -> str:
    match weight / height ** 2:
        case i if i <= 18.5:
            return "Underweight"
        case i if i <= 25.0:
            return "Normal"
        case i if i <= 30.0:
            return "Overweight"
        case _:
            return "Obese"


if __name__ == '__main__':
    print(bmi(47, 1.61))

    assert bmi(50, 1.80) == "Underweight"
    assert bmi(80, 1.80) == "Normal"
    assert bmi(90, 1.80) == "Overweight"
    assert bmi(110, 1.80) == "Obese"
    assert bmi(50, 1.50) == "Normal"
