
'''https://www.codewars.com/kata/55a75e2d0803fea18f00009d/train/python'''


def find_slope(points):
    a,b,c,d = points
    if c - a == 0:
        return "undefined"
    else:
        slope = (d - b) // (c - a)
    return str(slope)
