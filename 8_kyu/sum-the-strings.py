
'''https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python'''


def sum_str(a, b):
    if not a:a = '0'
    if not b:b = '0'
    return str(sum([int(a),int(b)]))