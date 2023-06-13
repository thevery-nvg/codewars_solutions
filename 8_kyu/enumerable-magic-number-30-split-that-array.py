
'''https://www.codewars.com/kata/545b342082e55dc9da000051/train/python'''


def partition(arr, c):
    a=list(filter(c,arr))
    return a,[x for x in arr if x not in a]