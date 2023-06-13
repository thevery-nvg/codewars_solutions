
'''https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python'''


def reverse_letter(string):
    return "".join([x for x in string[::-1] if x.isalpha()])

    