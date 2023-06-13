
'''https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python'''


def multi_table(number):
    return '\n'.join([f"{x} * {number} = {x*number}" for x in range(1,11)])