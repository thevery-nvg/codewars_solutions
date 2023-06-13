
'''https://www.codewars.com/kata/6324786fcc1a9700260a2147/train/python'''


def hyperfact(num):
    res = 1
    while num>0:
        res*=num**num
        num-=1
    return res%1000000007