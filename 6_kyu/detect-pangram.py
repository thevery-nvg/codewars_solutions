
'''https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python'''


def is_pangram(s):
    return len(set([x for x in s.lower() if 97<=ord(x)<=122]))==26