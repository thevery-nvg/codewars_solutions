
'''https://www.codewars.com/kata/58daa7617332e59593000006/train/python'''


def find_longest(arr):
    a = [len(str(x)) for x in arr]
    return arr[a.index(max(a))]