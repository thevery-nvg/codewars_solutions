
'''https://www.codewars.com/kata/54e6533c92449cc251001667/train/python'''


def unique_in_order(s):
    if not s:return []
    k = s[0]
    r =[k]
    for i in range(1,len(s)):
        if s[i]!= k:
            r.append(s[i])
            k =s[i]
    return r
            