
'''https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python'''


def vowel_one(s):

    return ''.join(['1' if x in 'euioa' else '0' for x in s.lower()])