
'''https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python'''


def flip(d, a):
    return sorted(a) if d=='R' else sorted(a,reverse=True)