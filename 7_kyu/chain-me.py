
'''https://www.codewars.com/kata/54fb853b2c8785dd5e000957/train/python'''


def chain(in_, func):
    if not func: return in_
    a = func[0](in_)
    for i in range(1,len(func)):
        a = func[i](a)
    return a
