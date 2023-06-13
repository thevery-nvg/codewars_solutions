
'''https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python'''


def accum(s):
    return '-'.join([f"{x.upper()}{x*(i)}" for i,x in enumerate(s.lower())])