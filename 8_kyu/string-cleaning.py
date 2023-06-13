
'''https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python'''


def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join(x for x in s if not x.isdigit())