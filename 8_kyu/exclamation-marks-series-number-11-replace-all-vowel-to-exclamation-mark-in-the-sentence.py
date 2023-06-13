
'''https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python'''


def replace_exclamation(s):
    return "".join('!'if x in 'aeiouAEIOU' else x for x in s)