
'''https://www.codewars.com/kata/57fae964d80daa229d000126/train/python'''


def remove(s):
    if not s: return s
    return s if s[-1] != '!' else s[:-1]