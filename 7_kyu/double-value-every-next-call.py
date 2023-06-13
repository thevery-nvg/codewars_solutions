
'''https://www.codewars.com/kata/632408defa1507004aa4f2b5/train/python'''


class Class:
    n=[0.5]
    @staticmethod
    def get_number():
        Class.n[0]*=2
        return Class.n[0]