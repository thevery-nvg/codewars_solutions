
'''https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python'''


def to_jaden_case(string):
    data = string.split(' ')
    for i in range(len(data)):
        data[i] = data[i].capitalize()
    string = ' '.join(data)
    return string