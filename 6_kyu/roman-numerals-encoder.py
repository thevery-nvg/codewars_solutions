
'''https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python'''


def solution(num):
        roman = {1: 'I',
                5: 'V', 4: 'IV',
                10: 'X', 9: 'IX',
                50: 'L', 40: 'XL',
                100: 'C', 90: 'XC',
                500: 'D', 400: 'CD',
                1000: 'M', 900: 'CM', }
        r = ''
        for n in sorted(roman, reverse=True):
            while n <= num:
                r += roman[n]
                num -= n
        return r