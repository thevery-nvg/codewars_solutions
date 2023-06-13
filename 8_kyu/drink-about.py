
'''https://www.codewars.com/kata/56170e844da7c6f647000063/train/python'''


def people_with_age_drink(age):
    return {age<14:'drink toddy',
            14<=age<18:'drink coke',
            18<=age<21:'drink beer',
            age>=21:'drink whisky'}[True]