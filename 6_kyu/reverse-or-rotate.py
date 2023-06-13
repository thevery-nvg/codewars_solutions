
'''https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python'''


def rev_rot(strng, sz):
    if sz<1:return ''
    temp= [strng[i:i+sz] for i in range(0,len(strng),sz) if len(strng[i:i+sz])==sz]
    def processing(a:str)->str:
        if sum(int(x) for x in a)%2==0:
            return a[::-1]
        else:return a[1:]+a[0]
    return ''.join(map(processing,temp))
        
        