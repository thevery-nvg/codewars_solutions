
'''https://www.codewars.com/kata/5a651865fd56cb55760000e0/train/python'''


def array_leaders(nums):
    r =[]
    for k in range(len(nums)):
        if nums[k]>sum(nums[k+1:]):
            r.append(nums[k])
    return r