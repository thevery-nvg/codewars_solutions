
'''https://www.codewars.com/kata/5761a717780f8950ce001473/train/python'''


def calculate_age(year_of_birth, current_year):
    d =current_year-year_of_birth
    s = '' if abs(d)==1 else 's'
    return f"You are {d} year{s} old." if d>0 else("You were born this very year!" if d ==0 else f"You will be born in {-d} year{s}.")