
'''https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/train/python'''


from math import pi
def area(f):
    if isinstance(f,tuple):
        return f[0]*f[1]
    else:
        return pi*f**2
        
def sort_by_area(seq): 
    return sorted(seq,key=area)
    