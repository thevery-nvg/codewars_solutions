
'''https://www.codewars.com/kata/5708f682c69b48047b000e07/train/python'''


def multiply(n):
    po = len(str(n)) if n>0 else len(str(n))-1
    return n*5**po