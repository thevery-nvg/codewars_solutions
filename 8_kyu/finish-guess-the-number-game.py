
'''https://www.codewars.com/kata/568018a64f35f0c613000054/train/python'''


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives < 1:
            raise ValueError('life goes down')
        if n != self.number:
            self.lives -= 1
            return False
        else:
            return True
        