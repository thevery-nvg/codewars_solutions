
'''https://www.codewars.com/kata/63f96036b15a210058300ca9/train/python'''


def second_symbol(s, symbol):
    if s.count(symbol)<=1:
        return -1
    return s.find(symbol,s.find(symbol)+1)