
'''https://www.codewars.com/kata/515e271a311df0350d00000f/train/python'''


def square_sum(numbers):
    return sum(map(pow,numbers,[2]*len(numbers)))