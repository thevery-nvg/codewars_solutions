
'''https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python'''


def first_non_consecutive(arr):
    r=[]
    for k in range(1,len(arr)):
        if arr[k]-1 != arr[k-1]:
            return arr[k]
    return None
            