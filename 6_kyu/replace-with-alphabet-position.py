
'''https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python'''


def alphabet_position(text):
    return ' '.join([str(ord(x.lower())-96) for x in text if 'a'<=x.lower()<='z'])