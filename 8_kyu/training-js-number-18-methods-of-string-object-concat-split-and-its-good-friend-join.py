
'''https://www.codewars.com/kata/57280481e8118511f7000ffa/train/python'''


def split_and_merge(s, se):
    return ' '.join([f"{se}".join(word) for word in s.split()])
