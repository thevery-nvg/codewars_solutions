
'''https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python'''


def solve(arr): 
    n=0
    while n<len(arr):
        while arr.count(arr[n])>1:
            arr.remove(arr[n])
        n+=1
    return arr
            