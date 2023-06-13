
'''https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python'''


def show_sequence(n):
    if n==0:return '0=0'
    if n<0:return f"{n}<0"
    s ='+'.join(map(str,range(n+1)))
    return f"{s} = {sum(map(int,s.split('+')))}"