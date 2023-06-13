
'''https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python'''


def count_positives_sum_negatives(arr):
    return [len(list(filter(lambda x:x>0,arr))),sum(filter(lambda x:x<0,arr))] if arr else arr