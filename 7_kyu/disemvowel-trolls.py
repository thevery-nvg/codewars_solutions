
'''https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python'''


def disemvowel(string_):
    return ''.join(x for x in string_ if x.lower() not in 'euioa')