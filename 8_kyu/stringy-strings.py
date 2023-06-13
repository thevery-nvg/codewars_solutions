
'''https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python'''


def stringy(size):
    return ''.join(['0' if x%2!=0 else '1' for x in range(size)])