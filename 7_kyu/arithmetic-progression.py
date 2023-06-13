
'''https://www.codewars.com/kata/55caf1fd8063ddfa8e000018/train/python'''


def arithmetic_sequence_elements(a, d, n):
    if d ==0:return ', '.join([str(a)]*n)
    return ', '.join([str(x) for x in range(a,a+d*n,d)])