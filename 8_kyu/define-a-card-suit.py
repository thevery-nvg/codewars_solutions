
'''https://www.codewars.com/kata/5a360620f28b82a711000047/train/python'''


def define_suit(card):
    return {"C":'clubs',"D":'diamonds','H':'hearts','S':'spades'}.get(card[-1],0)