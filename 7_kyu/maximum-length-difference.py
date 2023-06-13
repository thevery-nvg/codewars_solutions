
'''https://www.codewars.com/kata/5663f5305102699bad000056/train/python'''


def mxdiflg(a1, a2):
    if not a1 or not a2:return -1
    return max(len(max(a1,key=len)) -len(min(a2,key=len)),len(max(a2,key=len)) -len(min(a1,key=len))) 