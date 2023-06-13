
'''https://www.codewars.com/kata/5838a66eaed8c259df000003/train/python'''


def convert_palindromes(numbers):
    return [1 if str(x)==str(x)[::-1] else 0 for x in numbers]