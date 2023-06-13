
'''https://www.codewars.com/kata/59c8b38423dacc7d95000008/train/python'''


def isValid(f):
    valid = False
    if 1  in f and 2 in f:
        valid = False
    elif 3  in f and 4 in f:
        valid = False
    elif 5  in f :
        if 6 in f:
            valid = True
        else:valid = False
    elif 6  in f :
        if 5 in f:
            valid = True
        else:valid = False
    elif 7 in f or 8 in f:valid = True
    if 7 not in f and 8 not in f: valid =False
    
    return valid
    