
'''https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python'''


def fake_bin(x):
    re=''
    for i in x:
        if int(i)<5: re+='0'
        else: re += '1'
    return re
