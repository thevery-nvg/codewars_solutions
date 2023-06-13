
'''https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python'''


def distinct(seq):
    r = []
    for i in seq:
        if i not in r:
            r.append(i)
    return r