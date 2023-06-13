
'''https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python'''


def dirReduc(arr):
    di = {'north': 'south', 'east': 'west', 'west': 'east', 'south': 'north'}
    k = 0
    l = len(arr)
    while k < l:
        n = 1
        while n < len(arr):
            if di[arr[n].lower()] == arr[n - 1].lower():
                del arr[n]
                del arr[n - 1]
                break
            n += 1
        k += 1
    return arr