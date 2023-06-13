
'''https://www.codewars.com/kata/55960bbb182094bc4800007b/train/python'''


def insert_dash(num):
    s = [int(x) for x in str(num)]
    result =f'{s[0]}'
    for i in range(1,len(s)):
        if s[i-1] %2!= 0 and s[i]%2!=0:
            result+=f"-{s[i]}"
        else:
            result+=f"{s[i]}"
    return result
            
        
        

        
        

    