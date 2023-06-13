
'''https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python'''


def same_case(a, b): 
    if not a.isalpha() or not b.isalpha():
        return -1
    if a.isupper()^b.isupper():
        return 0
    else:return 1