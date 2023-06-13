
'''https://www.codewars.com/kata/5966f6343c0702d1dc00004c/train/python'''


def give_change(amount): 
    bills = (1,5,10,20,50,100)
    result =[0,0,0,0,0,0]
    p =5
    while p>-1:
        result[p]=amount//bills[p]
        amount = amount%bills[p]
        p-=1    
    return tuple(result)