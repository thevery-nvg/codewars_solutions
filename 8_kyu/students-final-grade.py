
'''https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python'''


def final_grade(ex, pr):
    if ex>90 or pr>10:
        return 100
    elif ex>75 and pr>=5:
        return 90
    elif ex>50 and pr>=2:
        return 75
    else: return 0