
'''https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python'''


import re
def validate_usr(username):
    if len(username) in range(4,17):
        pattern = r"^[a-z0-9_]+$"
        if re.match(pattern,username):
            return True
    return False
        