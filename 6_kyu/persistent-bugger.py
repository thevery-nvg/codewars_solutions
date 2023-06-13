
'''https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python'''


from functools import reduce
def persistence(n):
    k = 0
    while len(str(n))>1:
        n = str(reduce(lambda x,y:x*y,[int(a) for a in str(n)]))
        k+=1
    return k