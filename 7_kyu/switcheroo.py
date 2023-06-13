
'''https://www.codewars.com/kata/57f759bb664021a30300007d/train/python'''


def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))