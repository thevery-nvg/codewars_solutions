
'''https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python'''


def who_is_paying(name):
    return [name,name[:2]] if len(name)>2 else [name]