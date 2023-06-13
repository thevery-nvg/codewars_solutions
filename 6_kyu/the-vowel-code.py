
'''https://www.codewars.com/kata/53697be005f803751e0015aa/train/python'''


def encode(st):
    return st.translate(str.maketrans('aeiou','12345'))
    
def decode(st):
    return st.translate(str.maketrans('12345','aeiou'))