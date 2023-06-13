
'''https://www.codewars.com/kata/631f0c3a0b9cb0de6ded0529/train/python'''


def evaluate(eq):
    a = [int(x) for x in eq.split('@')]
    while len(a)>1:
        if a[1] == 0:
            return None
        a[:2] = [(a[0]+a[1])+(a[0]-a[1])+(a[0]*a[1])+(a[0]//a[1])]
    return a[0]
