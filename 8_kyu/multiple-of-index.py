
'''https://www.codewars.com/kata/5a34b80155519e1a00000009/train/python'''


def multiple_of_index(arr):
    return [x for i,x in enumerate(arr) if i>0 and x%i==0 ]