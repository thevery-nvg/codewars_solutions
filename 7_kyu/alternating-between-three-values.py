
'''https://www.codewars.com/kata/596776fbb4f24d0d82000141/train/python'''


def f(x, a, b, c): 
    l = [a,b,c]
    return l[l.index(x)+1] if l.index(x)+1<3 else l[0]
