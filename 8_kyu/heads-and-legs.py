
'''https://www.codewars.com/kata/574c5075d27783851800169e/train/python'''


def animals(heads, legs):
    a = (heads*4-legs)/2,(legs-heads*2)/2
    if int(a[0]) != int(a[0]) or int(a[1])!=a[1] or min(a)<0:
        return 'No solutions'
    else:
        return a