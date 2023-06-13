
'''https://www.codewars.com/kata/546e2562b03326a88e000020/train/python'''


def square_digits(num):
    return int(''.join(map(lambda x:str(int(x)**2),str(num))))