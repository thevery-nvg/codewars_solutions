
'''https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python'''


def two_highest(arg1):
    a = sorted(set(arg1),reverse = True)
    if not a : return []
    if len(a)==1: return [a[0]]
    return [a[0],a[1]] if a[0]!=a[1] else [a[0]] 