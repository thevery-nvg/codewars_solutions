
'''https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python'''


from collections import Counter
def find_it(seq):
    a = dict(Counter(seq))
    for i in a:
        if a[i]%2!= 0:
            return i
