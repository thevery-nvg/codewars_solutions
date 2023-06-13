
'''https://www.codewars.com/kata/56aed32a154d33a1f3000018/train/python'''


def my_first_kata(a,b):
    if isinstance(a,int) and isinstance(b,int):
        if a<=0 or b <=0:
            return False
        return a % b ++ b % a
    else:
        return False