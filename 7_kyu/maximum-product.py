
'''https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python'''


import math
def adjacent_element_product(ar):
    m = -math.inf
    for k in range(1,len(ar)):
        if ar[k-1]*ar[k] > m:
            m = ar[k-1]*ar[k]
    return m 
        