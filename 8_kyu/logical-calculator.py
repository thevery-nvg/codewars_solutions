
'''https://www.codewars.com/kata/57096af70dad013aa200007b/train/python'''


def logical_calc(array, op):
    match op:
        case "AND":op ='&'
        case "OR": op ='|'
        case "XOR":op = '^'
    r =array[0]
    for i in array[1:]:
        r = eval(str(r)+op+str(i))
    return r