
'''https://www.codewars.com/kata/555de49a04b7d1c13c00000e/train/python'''


def add(*args):
    return round(sum(x/(i+1) for i,x in enumerate(args)))