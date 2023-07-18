
'''https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/train/python'''


def find_array(arr1, arr2):
    res = []
    for i in arr2:
        try:
            res.append(arr1[i])
        except:
            pass
    return res