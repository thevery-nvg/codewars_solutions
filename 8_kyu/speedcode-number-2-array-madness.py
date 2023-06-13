
'''https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1/train/python'''


def array_madness(a,b):
    return sum(x*x for x in a)>sum(y**3 for y in b)