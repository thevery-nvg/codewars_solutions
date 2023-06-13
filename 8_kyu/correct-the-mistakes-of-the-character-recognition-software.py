
'''https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python'''


def correct(s):
    a = {"5":'S',"0":"O","1":"I"}
    return ''.join([(a[x] if x in a else x) for x in s])