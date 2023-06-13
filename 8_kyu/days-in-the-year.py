
'''https://www.codewars.com/kata/56d6c333c9ae3fc32800070f/train/python'''


def year_days(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return f"{year} has 366 days"
    else:
        return f"{year} has 365 days"