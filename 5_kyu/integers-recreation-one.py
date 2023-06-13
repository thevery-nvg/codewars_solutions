
'''https://www.codewars.com/kata/55aa075506463dac6600010d/train/python'''


def get_divizors(n):
    res = [n]
    for i in range(1, n//2+1):
        if n % i == 0:
            res.append(i)
    res = sum(map(lambda x: x * x, res))
    return res if int(res ** 0.5) == res ** 0.5 else None


def list_squared(m, n):
    res = []
    for x in range(m, n + 1):
        a = [x, get_divizors(x)] if get_divizors(x) else None
        if a:
            res.append(a)
    return res