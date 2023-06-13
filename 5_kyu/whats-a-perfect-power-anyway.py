
'''https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python'''


def isPP(n):
    def prime_generator(x):
        prs = {}
        p = 2
        while p < x:
            if p not in prs:
                yield p
                prs[p * p] = [p]
            else:
                for s in prs[p]:
                    prs.setdefault(s + p, []).append(s)
                del prs[p]
            p += 1
        
    def get_all_divisors_brute(n):
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                yield i
        yield n
    for n1 in get_all_divisors_brute(n):
        for k1 in prime_generator(100):
            if n1**k1==n:
                return [n1,k1]
    return None
    