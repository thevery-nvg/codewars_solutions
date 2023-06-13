
'''https://www.codewars.com/kata/542ebbdb494db239f8000046/train/python'''


import itertools
def next_item(xs, item):

    if type(xs)==type(iter(range(1))) or type(xs)== type(itertools.count(1)):
        for i in xs:
            if i ==item:
                return next(xs)
    for i,x in enumerate(xs):
        if x == item:
            return xs[i+1] if i+1<len(xs) else None
    return None