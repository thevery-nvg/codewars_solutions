
'''https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python'''


import re
def is_digit(n):
    if not n:return False
    if '\n' in n:return False
    print(f'"{n}"')
    print(bool(re.findall(r'^[0-9]?$',n)))
    return   bool(re.findall(r'^[0-9]?$',n))