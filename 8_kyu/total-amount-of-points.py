
'''https://www.codewars.com/kata/5bb904724c47249b10000131/train/python'''


def points(games):
    pnt = 0
    for r in games:
        if int(r[0])>int(r[2]):
            pnt += 3
        elif int(r[0])==int(r[2]):
            pnt += 1
    return pnt
            