
'''https://www.codewars.com/kata/58dced7b702b805b200000be/train/python'''


import math
def distance_between_points(a, b):
    a = a.x,a.y
    b= b.x,b.y
    return math.dist(a,b)
