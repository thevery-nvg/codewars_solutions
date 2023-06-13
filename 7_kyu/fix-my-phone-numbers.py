
'''https://www.codewars.com/kata/596343a24489a8b2a00000a2/train/python'''


import re
def is_it_a_num(s: str) -> str:
    number = "".join(re.findall(r'\d',s))
    return number if re.fullmatch(r'^0\d{10}',number) else 'Not a phone number'