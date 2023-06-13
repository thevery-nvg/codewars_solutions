
'''https://www.codewars.com/kata/5547929140907378f9000039/train/python'''


def shortcut( s ):
    dict = 'aeiou'
    return ''.join(list(filter(lambda x: x not in dict,s)))