
'''https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python'''


def solve(arr):
    res = []
    for s in arr:
        res.append(sum(1 for i,x in enumerate(s.lower()) if ord(x)-97==i))
    return res