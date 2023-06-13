
'''https://www.codewars.com/kata/53d16bd82578b1fb5b00128c/train/python'''


def grader(s):
    if s>1 or s<0.6: return "F"
    elif s>=0.9:return "A"
    elif s>=0.8:return "B"
    elif s>=0.7:return "C"
    elif s>=0.6:return "D"
