
'''https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python'''


def flatten_and_sort(array):
    res =[]
    for a in array:
        res.extend(a)
    return sorted(res)