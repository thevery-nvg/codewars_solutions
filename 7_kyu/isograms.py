
'''https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python'''


def is_isogram(s):
    return len(s)==len(set(s.lower()))