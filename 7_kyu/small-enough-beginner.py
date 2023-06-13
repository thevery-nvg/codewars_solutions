
'''https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python'''


def small_enough(array, limit):
    return len([x for x in array if x<=limit])==len(array)