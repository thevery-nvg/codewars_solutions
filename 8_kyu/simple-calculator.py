
'''https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python'''


def calculator(x,y,op):
    if type(x) == int:
        if type(y)==int:
            if type(op)==str and op in '/*-+':
                return eval(f'{x}{op}{y}')
    return "unknown value"