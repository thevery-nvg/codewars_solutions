
'''https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python'''


def high(x):
    y =[]
    words = x.split()
    for  k in words:
        y.append(sum(ord(a)-96 for a in k))
    return words[y.index(max(y))]