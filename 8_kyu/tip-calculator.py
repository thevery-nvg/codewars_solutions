
'''https://www.codewars.com/kata/56598d8076ee7a0759000087/train/python'''


import math
def calculate_tip(a, rating):
    a= {'poor':a*0.05,
                  'terrible':0,
                  'good':a*0.1,
                  'great':a*0.15,
                  'excellent':a*0.2
                 }.get(rating.lower(),"Rating not recognised")
    if type(a)==str:
        return a
    else:return math.ceil(a)