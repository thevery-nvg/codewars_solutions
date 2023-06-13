
'''https://www.codewars.com/kata/54edbc7200b811e956000556/train/python'''


def count_sheeps(sheep):
    k = 0
    for m in sheep:
        if m:
            k+=1
    return k