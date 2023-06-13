
'''https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python'''


def add_length(strng):
    return list(map(lambda x:f'{x} {len(x)}',strng.split()))