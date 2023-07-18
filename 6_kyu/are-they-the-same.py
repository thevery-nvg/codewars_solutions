
'''https://www.codewars.com/kata/550498447451fbbd7600041c/train/python'''


def comp(a, b):
    if a and b:
        if len(a)==len(b):
            return sorted([x**2 for x in a]) == sorted(b)
        else:
            return False
    if type(a)==type(b):
        if len(a)==len(b):
            return True
    return False
    