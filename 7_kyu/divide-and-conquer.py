
'''https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python'''


def div_con(x):
    return sum(num for num in x if isinstance(num,int))-sum(int(s) for s in x if isinstance(s,str))