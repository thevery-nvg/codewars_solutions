
'''https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python'''


def DNA_strand(dna):
    a = str.maketrans('ATTACGGC','TAATGCCG')
    return dna.translate(a)
