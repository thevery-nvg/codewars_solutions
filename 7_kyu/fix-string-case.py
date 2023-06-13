
'''https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python'''


def solve(s):
    l = sum(1 for letter in s if letter.islower())
    u = sum(1 for letter in s if letter.isupper())
    return s.upper() if u > l else s.lower()