
'''https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python'''


def pig_it(text):
    text = text.split(' ')
    for i in range(len(text)):
        end = '' if  '?' in text[i] or '!' in text[i]  else 'ay'
        text[i] = text[i][1:]+text[i][0]+end
    text = ' '.join(text)
    return text