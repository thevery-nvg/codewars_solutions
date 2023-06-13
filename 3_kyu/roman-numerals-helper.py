
'''https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python'''


class RomanNumerals:

    def to_roman(val):
        roman = {1: 'I',
                 5: 'V', 4: 'IV',
                 10: 'X', 9: 'IX',
                 50: 'L', 40: 'XL',
                 100: 'C', 90: 'XC',
                 500: 'D', 400: 'CD',
                 1000: 'M', 900: 'CM', }
        res = ''
        for n in sorted(roman, reverse=True):
            while n <= val:
                val -= n
                res += roman[n]
        return res


    def from_roman(roman_num):
        rom = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        temp = roman_num[::-1]
        res = 0
        n = 1
        while n < len(temp):
            if rom[temp[n]] < rom[temp[n - 1]]:
                res -= rom[temp[n]]
            else:
                res += rom[temp[n]]
            n += 1
        res += rom[temp[0]]
        return res