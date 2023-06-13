
'''https://www.codewars.com/kata/55ee3ebff71e82a30000006a/train/python'''


def title_to_number(title):
    r = 0
    for i in range(len(title)):
        r = r*26+(ord(title[i])-ord('A')+1)
    return r