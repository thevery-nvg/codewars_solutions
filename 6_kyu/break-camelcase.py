
'''https://www.codewars.com/kata/5208f99aee097e6552000148/train/python'''


def solution(s):
    l =s[0]
    for i in range(1,len(s)):
        if s[i-1].islower() and s[i].isupper():
            l+=' '+s[i]
        else:l+=s[i]
    return l
            

        