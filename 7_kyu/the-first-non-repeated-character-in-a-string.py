
'''https://www.codewars.com/kata/570f6436b29c708a32000826/train/python'''


def first_non_repeated(s):
    for i in s:
        if s.count(i)==1:
            return i
    return None