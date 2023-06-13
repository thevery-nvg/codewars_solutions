
'''https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python'''


def find_multiples(integer, limit):
    n= 1
    result = []
    while integer *n<=limit:
        result.append(integer *n)
        n+=1
    return result

        