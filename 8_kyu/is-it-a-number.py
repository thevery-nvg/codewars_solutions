
'''https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python'''


def isDigit(string):
    try: float(string.strip())
    except: return False
    else: return True

    
    