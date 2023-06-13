
'''https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python'''


def alias_gen(f_name, l_name):
    denied = "Your name must start with a letter from A - Z."
    f = FIRST_NAME.get(f_name[0].upper(),denied)
    s = SURNAME.get(l_name[0].upper(),denied)
    if s == denied or f == denied:
        return denied
    else:
        return f"{f} {s}"
