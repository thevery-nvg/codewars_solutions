
'''https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python'''


def array(string):
    r = ' '.join(string.split(',')[1:-1])
    return r if r else None