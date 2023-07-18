
'''https://www.codewars.com/kata/5adadcb36edb07df5600092e/train/python'''


def seven_wonders_science(c, g, t):
    ar= [c,g,t]
    points = sum(x**2 for x in ar)
    while all(ar):
        points +=7
        ar = [x-1 for x in ar]
        
    
    return points
