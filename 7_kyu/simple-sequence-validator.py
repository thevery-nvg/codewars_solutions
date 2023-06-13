
'''https://www.codewars.com/kata/553f01db29490a69ff000049/train/python'''


def validate_sequence(s):
    pattern = s[1]-s[0]
    for i in range(2,len(s)):
        if s[i-1]+pattern != s[i]:
            return False
    return True
        