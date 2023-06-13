
'''https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python'''


def dig_pow(n, p):
    n = str(n)
    s = 0
    for i in n:
        s += int(i)**p
        p+=1
    for i in range(s):
        a = int(n)*i
        if a == s:
            return i
        elif a > s:
            return -1