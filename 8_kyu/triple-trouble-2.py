
'''https://www.codewars.com/kata/5704aea738428f4d30000914/train/python'''


def triple_trouble(one, two, three):
    r =[]
    for a,b,c in zip(one,two,three):
        r.append(''.join((a,b,c)))
    return ''.join(r)
        