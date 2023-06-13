
'''https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python'''


def two_sum(nums, target):
        d = {}
        for i, j in enumerate(nums): # i - index, j - value
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i

        