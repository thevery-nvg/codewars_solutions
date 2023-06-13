
'''https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python'''


def bouncing_ball(h, bounce, window):
    if bounce >=1:return -1
    if h*bounce <window: return -1
    k=1
    while h*bounce >window:
        k+=2
        h *=bounce
    return k