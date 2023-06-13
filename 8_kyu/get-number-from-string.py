
'''https://www.codewars.com/kata/57a37f3cbb99449513000cd8/train/python'''


import re
def get_number_from_string(string):
    p = r"\d"
    return int(''.join(re.findall(p,string)))