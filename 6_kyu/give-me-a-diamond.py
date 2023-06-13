
'''https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python'''


def diamond(n):
    if n<=0:return None
    if n%2 ==0 :return None
    return  '\n'.join([f'{"*" * i:^{n}}'.rstrip() for i in range(1, n, 2)]+[f'{"*" * i:^{n}}'.rstrip() for i in range(n, 0, -2)])+'\n'