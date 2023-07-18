
'''https://www.codewars.com/kata/605f5d33f38ca800322cb18f/train/python'''


from string import ascii_lowercase
def tap_code_translation(text):
    letters = list(ascii_lowercase.replace('k',''))
    d={'k':(1,3)}
    for row in range(1,6):
        for col in range(1,6):
            d[letters.pop(0)]=(row,col)
    res= []
    for i in text:
        res.append(f"{'.'*d[i][0]} {'.'*d[i][1]}")
    return ' '.join(res)
            
            
    