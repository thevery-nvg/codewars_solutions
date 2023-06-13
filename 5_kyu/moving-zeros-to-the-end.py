
'''https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python'''


def move_zeros(nums):
    p = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[p] = nums[i]
            if i > p:
                nums[i] = 0
            p += 1
    return nums