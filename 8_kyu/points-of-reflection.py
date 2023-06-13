
'''https://www.codewars.com/kata/57bfea4cb19505912900012c/train/python'''


def symmetric_point(p, q):
    deltaX = abs(p[0]-q[0])*2
    deltaY = abs(p[1]-q[1])*2
    if p[0]>q[0] and p[1]>q[1]:
        return [p[0]-deltaX,p[1]-deltaY]
    elif p[0]<q[0] and p[1]<q[1]:
        return [p[0]+deltaX,p[1]+deltaY]
    elif p[0]>q[0] and p[1]<q[1]:
        return [p[0]-deltaX,p[1]+deltaY]
    elif p[0]<q[0] and p[1]>q[1]:
        return [p[0]+deltaX,p[1]-deltaY]
    else:return [0,0]