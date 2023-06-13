
'''https://www.codewars.com/kata/53d32bea2f2a21f666000256/train/python'''


import heapq
def largest(n, xs):
    return sorted(heapq.nlargest(n,xs))