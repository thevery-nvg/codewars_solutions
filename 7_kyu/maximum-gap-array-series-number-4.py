
'''https://www.codewars.com/kata/5a7893ef0025e9eb50000013/train/python'''


import math
def max_gap(n):
    n.sort()
    max_dist = 0
    for k in range(1,len(n)):
        x =n[k]
        y = n[k-1]
        if math.dist([x],[y])> max_dist:
            max_dist = math.dist([x],[y])
    return int(max_dist)
        
        