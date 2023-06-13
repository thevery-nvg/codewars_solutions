
'''https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python'''


import re
def domain_name(url):
    print(url)
    p =r"(\/|www\.)?(www\.)?([a-z0-9_-]{3,})(\.)"
    return re.search(p,url).group(3)