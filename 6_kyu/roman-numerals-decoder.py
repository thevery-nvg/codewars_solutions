
'''https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python'''


def solution(s):
        rom = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        temp = s[::-1]
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