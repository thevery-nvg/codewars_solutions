
'''https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python'''


def words_to_marks(s):
    return sum(ord(x)-96 for x in s)