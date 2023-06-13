
'''https://www.codewars.com/kata/57faece99610ced690000165/train/python'''


def remove(s):
    k = len(s)-1
    while s[k]=='!':
        k-=1
    return s[:k+1]
