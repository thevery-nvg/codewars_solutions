
'''https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python'''


def open_or_senior(data):
    return ["Senior" if (x[0]>=55 and x[1]>7) else "Open" for x in data]