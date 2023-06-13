
'''https://www.codewars.com/kata/5912ded3f9f87fd271000120/train/python'''


def count_correct_characters(correct, guess):
    if len(correct)== len(guess):
        return sum([1 for x,y in zip(correct,guess) if x==y])
    raise Error

    