
'''https://www.codewars.com/kata/59126992f9f87fd31600009b/train/python'''


def whoseMove(lastPlayer, win):
    if win:
        return lastPlayer
    else:
        return "white" if lastPlayer == "black" else "black"
