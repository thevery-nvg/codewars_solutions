
'''https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python'''


def longest_consec(arr, k):
    if k>len(arr) or k<1 or not arr:return ''
    m =0
    r=''
    for i in range(len(arr)):
        if sum(len(x) for x in arr[i:i+k])>m:
            m = sum(len(x) for x in arr[i:i+k])
            r = "".join(arr[i:i+k])
    return r

        