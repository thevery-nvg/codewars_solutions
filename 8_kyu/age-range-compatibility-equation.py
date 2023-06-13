
'''https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/python'''


def dating_range(age):
    if age <= 14:
        minimum_age = int(age - 0.10 * age)
        maximum_age = int(age + 0.10 * age)
    else:
        minimum_age = int(age / 2 + 7)
        maximum_age = int((age - 7) * 2)
    return f"{minimum_age}-{maximum_age}"