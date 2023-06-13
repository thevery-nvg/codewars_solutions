
'''https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python'''


def alphabet_war(fi):
    left_side = {'w':4,'p':3,'b':2,'s':1}
    right_side ={'m':4,'q':3,'d':2,'z':1}
    r = sum([right_side.get(x,0) for x in fi])
    l = sum([left_side.get(x,0) for x in fi])
    if l>r:
        return "Left side wins!"
    if r>l:
        return "Right side wins!"
    else: return "Let's fight again!"
    