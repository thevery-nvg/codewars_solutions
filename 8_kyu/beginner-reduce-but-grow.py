
'''https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python'''


def grow(arr):
    from functools import reduce
    return reduce(lambda x,y:x*y,arr)
