
'''https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python'''


import re
def increment_string(strng):
    def add_one(n: str) -> str:
        l = len(n)
        num = str(int(n)+1)
        if len(num) >= l:
            return num
        else:
            return f"{'0' * (l - len(num))}{num}"
    a = re.findall(r'\d+$',strng)
    if not a:
        return f"{strng}1"
    x = len(a[0])
    return strng[:-x]+add_one(a[0])

