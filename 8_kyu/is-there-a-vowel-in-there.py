
'''https://www.codewars.com/kata/57cff961eca260b71900008f/train/python'''


def is_vow(inp):
    cb = {ord(x):x for x in 'aeiou'}
    return list(map(lambda x:cb[x] if x in cb else x,inp))