
'''https://www.codewars.com/kata/55cb854deb36f11f130000e1/train/python'''


def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return (f"{c} is freezing temperature")
    else:
        return (f"{c} is above freezing temperature")
    
def convert_to_celsius (fahrenheit):
    return (fahrenheit - 32) * (5/9)
