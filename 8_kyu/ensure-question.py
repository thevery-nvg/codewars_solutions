
'''https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python'''


def ensure_question(s):
    return f"{s}?" if not s.endswith('?') else s