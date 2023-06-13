
'''https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python'''


def binary_array_to_number(arr):
     return int(''.join([str(x) for x in arr]),2)