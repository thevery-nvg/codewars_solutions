
'''https://www.codewars.com/kata/530e15517bc88ac656000716/train/python'''


import string
def rot13(msg):
    r= ''
    for x in msg:
        if x in string.ascii_letters:
            cs = x.islower()
            a = chr(ord(x.lower())+13) if ord(x.lower())<110 else chr(ord(x.lower())-13)
            if not cs:
                a = a.upper()
            r+=a
        else: r+=x
    return r
