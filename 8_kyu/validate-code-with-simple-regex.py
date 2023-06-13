
'''https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python'''


import re
def validate_code(code):
    p = r"^[1-3]"
    if re.match(p,str(code)):
        return True
    return False
        