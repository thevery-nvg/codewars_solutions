
'''https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python'''


def generate_shape(n):
    return '\n'.join([f"{'+'*n}" for _ in range(n)])