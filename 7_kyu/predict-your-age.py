
'''https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python'''


def predict_age(*ages):
    return int((sum(x*x for x in ages)**0.5)/2)