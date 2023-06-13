
'''https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python'''


def sum_array(arr):
    return sum(arr)-max(arr)-min(arr) if arr and len(arr)>1 else 0