
'''https://www.codewars.com/kata/559cc2d2b802a5c94700000c/train/python'''


def consecutive(arr):
    if len(arr)<2:return 0
    return len(range(min(arr),max(arr)+1))-len(arr)