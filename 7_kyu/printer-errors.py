
'''https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python'''


def printer_error(s):
    a = [chr(x) for x in range(ord('a'),ord('m')+1)]
    counter = 0
    for letter in s:
        if letter not in a:
            counter +=1
    return f"{counter}/{len(s)}"           
