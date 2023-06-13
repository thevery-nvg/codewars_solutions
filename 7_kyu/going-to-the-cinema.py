
'''https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/python'''


import math
def movie(card, ticket, perc):
    costA = n = 0
    costB = card
    while math.ceil(costB)>=costA:
        n+=1
        costA+=ticket
        costB+=ticket*math.pow(perc,n)
    return n