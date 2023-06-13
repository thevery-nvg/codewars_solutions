
'''https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python'''


def nb_year(p0, percent, aug, p):
    percent/=100
    n=0
    while p0< p:
        p0+=int(p0*percent)+aug
        n+=1
    return n