
'''https://www.codewars.com/kata/562926c855ca9fdc4800005b/train/python'''


def number_to_pwr(number, p): 
    if p == 0:return 1
    n = number
    for _ in range(p-1):
        number*=n
    return number