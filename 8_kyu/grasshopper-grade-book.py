
'''https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python'''


def get_grade(*a):
    score = sum(a)/3
    if 90 <= score <= 100: return 'A'
    elif 80 <= score < 90: return 'B'
    elif 70 <= score < 80: return 'C'
    elif 60 <= score < 70: return 'D'
    elif 0 <= score < 60: return 'F'

        
        
    