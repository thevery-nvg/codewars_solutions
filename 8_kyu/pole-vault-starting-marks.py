
'''https://www.codewars.com/kata/5786f8404c4709148f0006bf/train/python'''


def starting_mark(height):
    shorter_height = 1.52
    shorter_mark = 9.45
    
    rate_of_change = (10.67 - shorter_mark) / (1.83 - shorter_height)
    constant_offset = shorter_mark - rate_of_change * shorter_height
    
    return round(rate_of_change * height + constant_offset, 2)
