
'''https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python'''


def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    r = range(a, b + 1) if b > a else range(b, a + 1)
    x = 0
    for k in r:
        x+= k
    return x