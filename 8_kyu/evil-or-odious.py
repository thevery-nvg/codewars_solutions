
'''https://www.codewars.com/kata/56fcfad9c7e1fa2472000034/train/python'''


def evil(n):
    return "It's Evil!" if bin(n).replace('0b','').count('1')%2==0 else "It's Odious!"