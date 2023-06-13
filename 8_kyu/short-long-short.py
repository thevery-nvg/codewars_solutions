
'''https://www.codewars.com/kata/50654ddff44f800200000007/train/python'''


def solution(a, b):
    return f'{a}{b}{a}' if len(a)<len(b) else f'{b}{a}{b}'
