
'''https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python'''


def meeting(s):
    s = (tuple(a.upper().split(':')[::-1]) for a in s.split(";"))
    s  =  sorted(s,key = lambda x:(x[0],x[1]))
    s = map(str,s)
    s= ','.join(s).replace("'","")
    s = s.replace("),(",")(")
    return s
    
