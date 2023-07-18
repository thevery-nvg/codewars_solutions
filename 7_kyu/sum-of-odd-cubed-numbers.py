
'''https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python'''


def cube_odd(arr):
    if any(isinstance(x,bool) for x in arr):
        return None
    if all(isinstance(x,int) for x in arr):
        return sum(x**3 for x in arr if x&1)
