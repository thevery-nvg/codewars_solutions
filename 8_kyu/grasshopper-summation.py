
'''https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python'''


def summation(num):
    from functools import reduce
    return reduce(lambda x,y:x+y,range(num+1))
    
