
'''https://www.codewars.com/kata/556deca17c58da83c00002db/train/python'''


def tribonacci(signature, n):
    if n<3:
        return signature[:n]
    while len(signature) < n:
        signature.append(sum(signature[-1:-4:-1]))
    return signature