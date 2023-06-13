
'''https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python'''


def get_count(s):
    return sum([s.count(a) for a in "aeiou"])