
'''https://www.codewars.com/kata/5a905c2157c562994900009d/train/python'''


from functools import reduce
def product_array(n):
    return [reduce(lambda a,b:a*b,n[:i]+n[i+1:]) for i,x in enumerate(n)]