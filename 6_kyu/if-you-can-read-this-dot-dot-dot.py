
'''https://www.codewars.com/kata/586538146b56991861000293/train/python'''


def to_nato(words):
    return ' '.join([NATO[x] if x in NATO else x for x in words.upper() if x != ' '])