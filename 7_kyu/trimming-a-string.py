
'''https://www.codewars.com/kata/563fb342f47611dae800003c/train/python'''


def trim(phrase, size):
    if size<3:
        return f"{phrase[0:size]}..."
    if size ==3 and len(phrase)>3:
        return f"{phrase[0:size]}..."
    if len(phrase)<=size:
        return f"{phrase}"
    return f"{phrase[:size-3]}..."
