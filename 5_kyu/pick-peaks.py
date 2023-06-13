
'''https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python'''


def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    if not arr:
        return result
    n = 1
    while n < len(arr)-1 :
        if arr[n] > arr[n - 1] and arr[n] > arr[n + 1]:
            result['pos'].append(n)
            result['peaks'].append(arr[n])
        elif arr[n] > arr[n - 1] and arr[n] == arr[n + 1]:
            k = n + 1
            if k >= len(arr):
                return result
            while arr[n] == arr[k]:
                k += 1
                if k == len(arr):return result
            if arr[k] < arr[n]:
                result['pos'].append(n)
                result['peaks'].append(arr[n])
            n = k-1
        n += 1
    return result
