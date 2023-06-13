
'''https://www.codewars.com/kata/5732d3c9791aafb0e4001236/train/python'''


from math import ceil,floor
def round_it(n):
    left,right = str(n).split('.')
    if len(left)>len(right):
        return floor(n)
    elif len(left)==len(right):
        return round(n)
    else:
        return ceil(n)
