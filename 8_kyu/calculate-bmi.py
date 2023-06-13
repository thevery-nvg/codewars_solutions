
'''https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python'''


def bmi(weight, height):
    bmi = weight/height**2
    return "Underweight" if bmi<=18.5 else ( "Normal" if bmi <=25.0 else( "Overweight" if bmi<= 30.0 else  "Obese") )