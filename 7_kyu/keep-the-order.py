
'''https://www.codewars.com/kata/582aafca2d44a4a4560000e7/train/python'''


def keep_order(arr, val):
    print(arr,val)
    if not arr:return 0
    if val<=arr[0]:return 0
    if val>arr[-1]:return len(arr)
    for i in range(len(arr)):
        if arr[i-1]<=val<=arr[i]:
            return i
    return 0
        
        
        