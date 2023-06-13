
'''https://www.codewars.com/kata/513e08acc600c94f01000001/train/python'''


def rgb(r, g, b):
    rounddown = lambda x: 0 if x < 0 else x
    r = 255 if r > 255 else rounddown(r)
    g = 255 if g > 255 else rounddown(g)
    b = 255 if b > 255 else rounddown(b)
    r = hex(r)[2:] if r > 15 else '0' + hex(r)[2:]
    g = hex(g)[2:] if g > 15 else '0' + hex(g)[2:]
    b = hex(b)[2:] if b > 15 else '0' + hex(b)[2:]
    return (r + g + b).upper()