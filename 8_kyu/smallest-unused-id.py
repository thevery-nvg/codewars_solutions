
'''https://www.codewars.com/kata/55eea63119278d571d00006a/train/python'''


def next_id(arr):
    if not arr:return 0
    
    a =set(arr)
    if max(a)+1 == len(a):return max(a)+1
    for i in range(max(a)+1):
        if not i in a:
            return i
    return max(a)+1
        
    
    