
'''https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python'''


def remainder(a,b):
    k = [a,b]
    if min(k)==0 in k:return None
    return max(k)%min(k)
    
    