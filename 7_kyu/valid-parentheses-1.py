
'''https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/python'''


def valid_parentheses(paren_str):
    stack = []
    for i in paren_str:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return stack == []
