
'''https://www.codewars.com/kata/545af3d185166a3dec001190/train/python'''


def each_cons(lst, n):
    r = []
    for i,j in zip(range(len(lst)),range(n,len(lst)+1)):
        r.append(lst[i:j])
    return r
        
    