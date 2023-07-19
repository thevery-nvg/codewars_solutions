
'''https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python'''


def move_zeros(nums):
    return sorted(nums,key=lambda x:x==0)