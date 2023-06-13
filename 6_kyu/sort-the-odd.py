
'''https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python'''


def sort_array(arr):
    even={}
    odd =[]
    result =[0]*len(arr)
    for i,j in enumerate(arr):
        if j%2==0:
            even[i]=j
        else:
            odd.append(j)
    odd.sort()
    for k in even:
        odd.insert(k,even[k])
    return odd
            