
'''https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python'''


def find_nb(m):
    sum_cubes = 0
    n = 1
    while sum_cubes<m:
        sum_cubes+=n**3
        if sum_cubes == m:
            return n
        n+=1
    return -1
        
