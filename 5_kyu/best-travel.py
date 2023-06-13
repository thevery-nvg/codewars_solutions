
'''https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python'''


def choose_best_sum(t, k, ls):
    import itertools
    ways = itertools.combinations(ls, k)
    m = 0
    for k in ways:
        a= sum(k)
        if a > m and a <= t:
            m = a
    return m if m > 0 else None