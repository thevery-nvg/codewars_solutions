
'''https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python'''


def order(sentence):
    def numsort(s):
        for i in s:
            if i.isdecimal():
                return int(i)
    return ' '.join(sorted(sentence.split(),key=numsort))