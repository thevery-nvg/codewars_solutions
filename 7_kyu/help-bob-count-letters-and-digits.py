
'''https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python'''


import re
def count_letters_and_digits(s):
    return len(re.findall(r'[a-zA-Z0-9]',s))