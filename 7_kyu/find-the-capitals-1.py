
'''https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python'''


def capitals(word):
    return [i for i,a in enumerate(word) if a.isupper()]