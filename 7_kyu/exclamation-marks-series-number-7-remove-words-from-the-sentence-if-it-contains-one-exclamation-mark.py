
'''https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python'''


def remove(s):
    return ' '.join(x for x in s.split() if x.count('!')!=1)