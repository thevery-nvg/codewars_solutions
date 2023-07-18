
'''https://www.codewars.com/kata/557af4c6169ac832300000ba/train/python'''


import re
def remove_rotten(b):
    if b:
        p=re.compile(r'(?P<rot>rotten)?(?P<fruit>\w+)')
        return [p.search(f).group('fruit').lower() for f in b]
    return []
        
    