
'''https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python'''


def min_value(digits):
    return int(''.join(str(x) for x in sorted(set(digits))))