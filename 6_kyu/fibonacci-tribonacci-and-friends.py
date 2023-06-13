
'''https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python'''


from collections import deque
def Xbonacci(signature,n):
    print(signature,n)
    if n<len(signature):return signature[:n]
    result = signature
    sign = deque(signature,maxlen = len(signature))
    while len(result)<n:
        next = sum(sign)
        result.append(next)
        sign.append(next)
    return result