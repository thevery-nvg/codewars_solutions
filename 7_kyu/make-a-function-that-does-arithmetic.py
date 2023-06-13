
'''https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python'''


def arithmetic(a, b, operator):
    match operator:
        case "add":return a+b
        case "subtract":return a-b
        case "multiply":return a*b
        case "divide":return a/b