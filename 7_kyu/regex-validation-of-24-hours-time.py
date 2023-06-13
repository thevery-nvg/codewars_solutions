
'''https://www.codewars.com/kata/56a4a3d4043c316002000042/train/python'''


import re
def validate_time(time):
    if re.match(r'^\d{1,2}:\d{2}',time):
        h,m = time.split(':')
        if int(h)in range(24) and int(m) in range(60):
            return True
    return False
        