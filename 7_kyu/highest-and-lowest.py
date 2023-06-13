
'''https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python'''


def high_and_low(nums):
    nums = [int(a) for a in nums.split()]
    return ' '.join([str(max(nums)),str(min(nums))])