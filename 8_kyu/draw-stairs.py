
'''https://www.codewars.com/kata/5b4e779c578c6a898e0005c5/train/python'''


def draw_stairs(n):
    return '\n'.join(f'{" "*x}I'for x in range(n))