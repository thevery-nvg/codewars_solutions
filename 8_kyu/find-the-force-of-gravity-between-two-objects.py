
'''https://www.codewars.com/kata/5b609ebc8f47bd595e000627/train/python'''


def solution(av, au) :
    G = 6.67e-11
    c = { 'kg':1, 'g':1e-3, 'mg':1e-6, 'μg':1e-9, 'lb':.453592
                     , 'm':1, 'cm':1e-2, 'mm':1e-3, 'μm':1e-6, 'ft':.3048
                     }
    return G*av[0]*c[au[0]]*av[1]*c[au[1]]/(av[2]*c[au[2]])**2