
'''https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python'''


def incrementer(nums):
    return [(x+i)%10 for i,x in enumerate(nums,1)]