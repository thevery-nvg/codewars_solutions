
'''https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python'''


from collections import Counter
def duplicate_encode(word):
    a =Counter(word.lower())
    for k in a:
        if a[k]>1:a[k]=")"
        else: a[k] = "("
    return ''.join(a[k] for k in word.lower())