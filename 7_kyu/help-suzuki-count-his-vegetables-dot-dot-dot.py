
'''https://www.codewars.com/kata/56ff1667cc08cacf4b00171b/train/python'''


def count_vegetables(string):
    r =[]
    s= string.split()
    a = set(s)
    for i in a:
        if i in ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]:
            r.append((string.count(i),i))
    return sorted(sorted(r,key=lambda x:x[1],reverse = True),key =lambda x:x[0],reverse = True)
    