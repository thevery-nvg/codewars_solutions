
'''https://www.codewars.com/kata/575fa9afee048b293e000287/train/python'''


def how_much_water(W,L,C):
    if C>2*L :return 'Too much clothes'
    if C<L:return 'Not enough clothes'
    return round(W*1.1**(C-L),2)