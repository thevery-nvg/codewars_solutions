
'''https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/python'''


def dominator(arr):
    if len(arr)==0:
        return -1
    if len(arr)==1:return arr[0]
    for i in range(len(arr)//2+2):
        if arr.count(arr[i])>=len(arr)//2+1:
            return arr[i]
    return -1