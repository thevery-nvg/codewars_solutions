
'''https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python'''


def are_you_playing_banjo(name):
    return f"{name}{' plays banjo' if name.lower().startswith('r') else ' does not play banjo'}"