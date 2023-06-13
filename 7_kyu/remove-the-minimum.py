
'''https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python'''


def remove_smallest(numbers):
    if not numbers:return []
    a = numbers.index(min(numbers)) 
    return numbers[:a]+numbers[a+1:]
