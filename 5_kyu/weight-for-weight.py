
'''https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python'''


def order_weight(strng):
    def findPlato(s):
        n = 1
        result = []
        while n < len(s):
            if s[n] == s[n - 1]:
                start = n - 1
                while s[n] == s[n - 1] and n < len(s) - 1:
                    n += 1
                end = n - 1
                result.append((start, end+1) if start != end else (start, end + 2))
            n += 1
        return result
    platos = findPlato(sorted(map(lambda x: sum(map(int, x)),strng.split())))

    res =sorted(strng.split(), key=lambda x: sum(map(int, x)))

    for k in platos:
        res[k[0]:k[1]] = sorted(res[k[0]:k[1]])
    return " ".join(res)