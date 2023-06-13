
'''https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python'''


def find_even_index(arr):
    #your code here
    n = 0
    while n < len(arr):
        if sum(arr[:n+1]) == sum(arr[n:]):
            return n
        n +=1
    else:
        return -1