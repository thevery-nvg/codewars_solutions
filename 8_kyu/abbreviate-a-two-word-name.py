
'''https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python'''


def abbrev_name(nm):
    return '.'.join([x[0].upper() for x in nm.split()])