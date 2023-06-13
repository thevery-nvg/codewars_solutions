
'''https://www.codewars.com/kata/635a7827bafe03708e3e1db6/train/python'''


def speed_limit(speed, signals):
    total = 0
    for s in signals:
        if speed - s in range(10,20):
            total += 100
        elif  speed - s in range(20,30):
            total+=250
        elif speed - s>=30:
            total +=500
        else:
            continue
    return total
        