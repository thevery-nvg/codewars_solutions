
'''https://www.codewars.com/kata/5951d30ce99cf2467e000013/train/python'''


# input is an unsorted list of 3 positive integers
def pythagorean_triple(i):
    i.sort()
    return i[0]**2+i[1]**2==i[2]**2
    