
'''https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python'''


def close_compare(a, b, margin=0):
    if abs(margin)>0 and  abs(a-b)<=abs(margin):
            return 0
    else:
        if a<b:return -1
        elif a>b: return 1
        else: return 0
            

    