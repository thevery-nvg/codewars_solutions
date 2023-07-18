
'''https://www.codewars.com/kata/526c7363236867513f0005ca/train/python'''


def isLeapYear(y):
    if y % 400 == 0 or y% 100 != 0 and y % 4 == 0:  
        return True
    return False


