
'''https://www.codewars.com/kata/582e0e592029ea10530009ce/train/python'''


def duck_duck_goose(pl, g):
    #a = min(len(pl),max([1,g]))
    if g>len(pl):
        g = g%len(pl)
    return pl[g-1].name