
'''https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python'''


from functools import reduce
def factorial(n):
    if n in range(1,13):
        return reduce(lambda x,y:x*y,range(1,n+1))
    elif n == 0:
        return 1
    else:
        raise ValueError