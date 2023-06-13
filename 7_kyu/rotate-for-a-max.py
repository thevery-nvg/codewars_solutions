
'''https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python'''


def max_rot(n):
    if n <10:return n
    a = list(str(n))
    end_list = [n]
    for i in range(8):
        x = a[i]
        del a[i]
        a.append(x)
        end_list.append(int(''.join(a)))
    print(end_list)
    return max(end_list)
        
        

    

    
    
    