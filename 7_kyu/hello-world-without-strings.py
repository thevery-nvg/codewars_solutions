
'''https://www.codewars.com/kata/584c7b1e2cb5e1a727000047/train/python'''


def hello_world():
    d = [101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    res = chr(72)
    for i in d:
        res+=chr(i)
    return res
    