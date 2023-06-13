
'''https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python'''


def declare_winner(fighter1, fighter2, first_attacker):
    if fighter2.name == first_attacker:
        fighter2,fighter1=fighter1,fighter2
    while True:
        fighter2.health=fighter2.health - fighter1.damage_per_attack
        if fighter2.health<=0:return fighter1.name
        fighter1.health=fighter1.health - fighter2.damage_per_attack
        if fighter1.health<=0:return fighter2.name

        