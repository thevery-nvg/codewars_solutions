
'''https://www.codewars.com/kata/636f26f52aae8fcf3fa35819/train/python'''


# return the total byte size of the object. 
def total_bytes(object):
    import sys
    return sys.getsizeof(object)