
'''https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python'''


from collections import Counter
def duplicate_count(text):
    a = Counter(text.lower())
    n=0
    for k in a:
        if a[k]>1:
            n+=1
    return n
     