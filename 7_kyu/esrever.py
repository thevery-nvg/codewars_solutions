
'''https://www.codewars.com/kata/5413759479ba273f8100003d/train/python'''


def reverse(lst):
    empty_list = list()  
    for i in lst:
        empty_list = [i]+empty_list
    return empty_list
    