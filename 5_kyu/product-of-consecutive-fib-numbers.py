
'''https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python'''


def productFib(prod):
    cache ={0:0}
    def fib(n):
        if n ==1:return 0
        a=0
        b=1
        for _ in range(n):
            a,b = b,a+b
        return b    
    for f in range(1,prod):
        cache[f] = fib(f)
        if cache[f-1]*cache[f]==prod:return  [cache[f-1],cache[f],True]
        elif cache[f-1]*cache[f]>prod: return [cache[f-1],cache[f],False]
    if prod == 0: return [0, 1, True]
    elif prod == 1: return [1, 1, True]
    elif prod ==2:return [1, 2, True]
    elif prod ==3: return [2, 3, False]

         
        
