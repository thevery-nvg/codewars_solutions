
'''https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python'''


from collections import Counter
def find_uniq(arr):
    a = Counter(arr)
    return a.most_common()[-1][0]