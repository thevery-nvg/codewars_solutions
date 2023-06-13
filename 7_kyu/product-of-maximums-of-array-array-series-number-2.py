
'''https://www.codewars.com/kata/5a63948acadebff56f000018/train/python'''


import heapq
from functools import reduce
def max_product(n_largest_elements,lst):
    return reduce(lambda x,y:x*y,heapq.nlargest(lst,n_largest_elements))