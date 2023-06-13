
'''https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python'''


def find_difference(a, b):
    from functools import reduce
    return abs(reduce(lambda x,y:x*y,a)-reduce(lambda x,y:x*y,b))