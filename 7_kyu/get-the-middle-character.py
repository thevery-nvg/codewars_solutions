
'''https://www.codewars.com/kata/56747fd5cb988479af000028/train/python'''


def get_middle(s):
    return s[len(s)//2] if len(s)%2!=0 else f"{s[len(s)//2-1]}{s[len(s)//2]}"