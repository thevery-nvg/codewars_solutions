
'''https://www.codewars.com/kata/595aa94353e43a8746000120/train/python'''


def find_deleted_number(arr, mixed_arr):
    if len(arr)==len(mixed_arr):return 0

    return list(set(arr)-set(mixed_arr))[0]