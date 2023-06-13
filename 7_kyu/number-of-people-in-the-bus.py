
'''https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python'''


def number(bus_stops):
    return sum(x[0]-x[1] for x in bus_stops)