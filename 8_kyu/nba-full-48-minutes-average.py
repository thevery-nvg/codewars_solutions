
'''https://www.codewars.com/kata/587c2d08bb65b5e8040004fd/train/python'''


def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0
    else:
        extrapolated_ppg = (ppg / mpg) * 48
        return round(extrapolated_ppg, 1)
