
'''https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python'''


import heapq
def largest_pair_sum(numbers): 
    return  sum(heapq.nlargest(2, numbers))