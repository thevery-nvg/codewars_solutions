
'''https://www.codewars.com/kata/57f609022f4d534f05000024/train/python'''


def stray(arr):
    x = arr[0]
    for i in arr[1:]:
        x^=i
    return x