
'''https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python'''


def rental_car_cost(d):
    return 40*d -50 if d>=7  else (40*d-20 if d >=3 else 40*d)